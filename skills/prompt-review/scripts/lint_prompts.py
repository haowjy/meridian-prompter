#!/usr/bin/env python3
"""Static linter for agent prompts, skills, and AGENTS.md files.

Enforces deterministic prompt-engineering invariants (1-level-deep progressive
disclosure, orphan/broken resources, Codex description budget, bare @ mentions,
uninvocable `available` skills, emphasis inflation, and line budgets) using
only the Python standard library.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

EXCLUDED_DIRS = {
    ".git",
    ".mars",
    ".claude",
    ".codex",
    ".cursor",
    ".opencode",
    ".pi",
    ".agents",
    "plugin",
    "node_modules",
    "target",
    ".venv",
    "__pycache__",
}

CODEX_DESC_BUDGET = 8000
MAX_SINGLE_DESC = 300
MAX_AGENTS_MD_LINES = 200
MAX_SKILL_MD_LINES = 500

RESOURCE_REF_RE = re.compile(r"resources/([A-Za-z0-9._/-]+\.md)")
CROSS_SKILL_PREFIX_RE = re.compile(
    r"(?:`/[a-z0-9_-]+`|`?[a-z0-9_-]+__meridian`?|\bmeridian skills\b)"
)
# Match bare @word outside emails/code (preceded by start/space/paren/bracket)
BARE_AT_RE = re.compile(r"(?:^|[\s(\[])@([A-Za-z][A-Za-z0-9._/-]{1,})")
EMPHASIS_RE = re.compile(r"\b(CRITICAL:|IMPORTANT:|YOU MUST\b|NEVER EVER\b)")
WEAK_HEDGE_RE = re.compile(r"\bif in doubt\b", re.IGNORECASE)


def find_local_resource_refs(text: str) -> set[str]:
    """Find resources/*.md references belonging to the current skill, skipping cross-skill refs."""
    collapsed = re.sub(r"\s+", " ", text)
    refs: set[str] = set()
    for m in RESOURCE_REF_RE.finditer(collapsed):
        # Split at sentence boundaries (". ", "; ") or ", then " so file extensions like ".md" don't split
        window = collapsed[max(0, m.start() - 160) : m.start()]
        clause = re.split(r"[.;](?:\s|$)|,\s+then\b", window)[-1]
        if CROSS_SKILL_PREFIX_RE.search(clause):
            continue
        refs.add(m.group(1))
    return refs


@dataclass
class Finding:
    severity: str  # "ERROR" or "WARN"
    code: str
    path: Path
    line: int | None
    message: str

    def format(self, root: Path) -> str:
        try:
            rel = self.path.relative_to(root)
        except ValueError:
            rel = self.path
        loc = f"{rel}:{self.line}" if self.line is not None else str(rel)
        return f"[{self.severity}] {self.code} {loc} — {self.message}"


def split_frontmatter(text: str) -> tuple[str, str, int]:
    """Return (frontmatter_text, body_text, body_start_line)."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return "", text, 1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1 :]), i + 2
    return "", text, 1


def parse_simple_frontmatter(fm: str) -> dict[str, object]:
    """Extract key fields from YAML frontmatter without requiring PyYAML."""
    result: dict[str, object] = {}
    lines = fm.splitlines()
    i = 0
    in_skills = False
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            i += 1
            continue

        # Top-level key
        if not line.startswith((" ", "\t")):
            in_skills = stripped.startswith("skills:")
            m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", stripped)
            if m:
                key, val = m.group(1), m.group(2).strip()
                if val in (">", "|", ">-", "|-"):
                    block: list[str] = []
                    i += 1
                    while i < len(lines) and (lines[i].startswith((" ", "\t")) or not lines[i].strip()):
                        block.append(lines[i].strip())
                        i += 1
                    result[key] = " ".join(p for p in block if p)
                    continue
                if val.startswith(('"', "'")) and val.endswith(('"', "'")) and len(val) >= 2:
                    val = val[1:-1]
                result[key] = val
        elif in_skills:
            m_avail = re.match(r"^\s+available:\s*\[([^\]]*)\]", line)
            if m_avail:
                items = [s.strip().strip("'\"") for s in m_avail.group(1).split(",") if s.strip()]
                result["skills.available"] = items
        i += 1
    return result


def iter_prose_lines(body: str, start_line: int) -> list[tuple[int, str]]:
    """Yield (line_no, line_without_inline_code) skipping fenced code blocks."""
    out: list[tuple[int, str]] = []
    in_fence = False
    for offset, line in enumerate(body.splitlines()):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        # Strip inline backtick spans so examples/code mentions don't false-positive
        cleaned = re.sub(r"`[^`]*`", "", line)
        out.append((start_line + offset, cleaned))
    return out


def walk_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for p in sorted(root.rglob("*.md")):
        rel_parts = p.relative_to(root).parts
        if any(part in EXCLUDED_DIRS for part in rel_parts):
            continue
        files.append(p)
    return files


def lint_package(root: Path) -> tuple[list[Finding], dict[str, int]]:
    findings: list[Finding] = []
    stats = {"agents": 0, "skills": 0, "agents_md": 0, "desc_chars": 0}

    skill_meta: dict[str, dict[str, object]] = {}
    skills_dir = root / "skills"
    if skills_dir.is_dir():
        for skill_md in sorted(skills_dir.glob("*/SKILL.md")):
            stats["skills"] += 1
            skill_dir = skill_md.parent
            text = skill_md.read_text(encoding="utf-8")
            fm_text, body, body_start = split_frontmatter(text)
            fm = parse_simple_frontmatter(fm_text)
            name = str(fm.get("name") or skill_dir.name)
            skill_meta[name] = fm

            # Description budget
            desc = str(fm.get("description") or "")
            stats["desc_chars"] += len(desc)
            if len(desc) > MAX_SINGLE_DESC:
                findings.append(
                    Finding(
                        "WARN",
                        "DESC_LENGTH",
                        skill_md,
                        1,
                        f"description is {len(desc)} chars (target <= {MAX_SINGLE_DESC})",
                    )
                )

            # Line budget
            line_count = len(text.splitlines())
            if line_count > MAX_SKILL_MD_LINES:
                findings.append(
                    Finding(
                        "WARN",
                        "LINE_BUDGET",
                        skill_md,
                        None,
                        f"SKILL.md is {line_count} lines (target <= {MAX_SKILL_MD_LINES})",
                    )
                )

            # Resource checks (1-level-deep & orphan/broken)
            refs_in_skill = find_local_resource_refs(body)
            resources_dir = skill_dir / "resources"
            disk_resources: set[str] = set()
            if resources_dir.is_dir():
                for res_file in sorted(resources_dir.rglob("*.md")):
                    rel_res = res_file.relative_to(resources_dir).as_posix()
                    disk_resources.add(rel_res)

                    # Multi-hop check: resource referencing another local resource
                    res_text = res_file.read_text(encoding="utf-8")
                    res_refs = find_local_resource_refs(res_text) - {rel_res}
                    if res_refs:
                        findings.append(
                            Finding(
                                "WARN",
                                "MULTI_HOP_RESOURCE",
                                res_file,
                                None,
                                f"links to other resources ({', '.join(sorted(res_refs))}); keep disclosure 1 level deep from SKILL.md",
                            )
                        )

                    # Prose lints inside resources
                    for line_no, prose in iter_prose_lines(res_text, 1):
                        check_prose_line(res_file, line_no, prose, findings, check_bare_at=True)

            for ref in sorted(refs_in_skill):
                if ref not in disk_resources:
                    findings.append(
                        Finding(
                            "ERROR",
                            "BROKEN_RESOURCE",
                            skill_md,
                            None,
                            f"references missing resource resources/{ref}",
                        )
                    )

            for orphan in sorted(disk_resources - refs_in_skill):
                findings.append(
                    Finding(
                        "ERROR",
                        "ORPHAN_RESOURCE",
                        resources_dir / orphan,
                        None,
                        f"not referenced in {skill_md.name} (agents will rarely discover it)",
                    )
                )

            # Prose lints in SKILL.md
            for line_no, prose in iter_prose_lines(body, body_start):
                check_prose_line(skill_md, line_no, prose, findings, check_bare_at=True)

            # Routing-only stub detection
            non_heading_body = "\n".join(
                ln for ln in body.splitlines() if ln.strip() and not ln.strip().startswith("#")
            )
            if len(non_heading_body) < 350 and ("meridian skills " in body or "resources/" in body):
                findings.append(
                    Finding(
                        "WARN",
                        "ROUTING_STUB",
                        skill_md,
                        body_start,
                        f"body is only {len(non_heading_body)} chars and routes elsewhere; point straight to the target",
                    )
                )

    if stats["desc_chars"] > CODEX_DESC_BUDGET:
        findings.append(
            Finding(
                "WARN",
                "DESC_BUDGET",
                root,
                None,
                f"total skill description length is {stats['desc_chars']} chars (exceeds Codex ~{CODEX_DESC_BUDGET}-char budget)",
            )
        )

    # Check agents/*.md
    agents_dir = root / "agents"
    if agents_dir.is_dir():
        for agent_md in sorted(agents_dir.glob("*.md")):
            stats["agents"] += 1
            text = agent_md.read_text(encoding="utf-8")
            fm_text, body, body_start = split_frontmatter(text)
            fm = parse_simple_frontmatter(fm_text)

            available = fm.get("skills.available")
            if isinstance(available, list):
                for skill_name in available:
                    meta = skill_meta.get(str(skill_name))
                    if meta and str(meta.get("model-invocable", "")).lower() == "false":
                        findings.append(
                            Finding(
                                "ERROR",
                                "UNINVOCABLE_AVAILABLE",
                                agent_md,
                                None,
                                f"lists `{skill_name}` in skills.available, but its SKILL.md has model-invocable: false",
                            )
                        )

            for line_no, prose in iter_prose_lines(body, body_start):
                check_prose_line(agent_md, line_no, prose, findings, check_bare_at=False)

    # Check AGENTS.md files
    for md_file in walk_files(root):
        if md_file.name != "AGENTS.md":
            continue
        stats["agents_md"] += 1
        text = md_file.read_text(encoding="utf-8")
        line_count = len(text.splitlines())
        if line_count > MAX_AGENTS_MD_LINES:
            findings.append(
                Finding(
                    "WARN",
                    "LINE_BUDGET",
                    md_file,
                    None,
                    f"AGENTS.md is {line_count} lines (target <= {MAX_AGENTS_MD_LINES})",
                )
            )
        for line_no, prose in iter_prose_lines(text, 1):
            check_prose_line(md_file, line_no, prose, findings, check_bare_at=True)

    return findings, stats


def check_prose_line(
    path: Path,
    line_no: int,
    prose: str,
    findings: list[Finding],
    *,
    check_bare_at: bool,
) -> None:
    if check_bare_at:
        for m in BARE_AT_RE.finditer(prose):
            token = m.group(1)
            # Ignore common scoped npm/version tokens like @latest or @types
            if token.startswith(("types/", "latest")):
                continue
            findings.append(
                Finding(
                    "ERROR",
                    "BARE_AT_MENTION",
                    path,
                    line_no,
                    f"bare @{token} can auto-load a file in Claude Code; use backticks without @",
                )
            )
    unquoted = re.sub(r'"[^"]*"', "", prose)
    if EMPHASIS_RE.search(unquoted):
        findings.append(
            Finding(
                "WARN",
                "EMPHASIS_INFLATION",
                path,
                line_no,
                "ALL-CAPS emphasis (CRITICAL/IMPORTANT/YOU MUST) causes overtriggering on current models",
            )
        )
    if WEAK_HEDGE_RE.search(unquoted):
        findings.append(
            Finding(
                "WARN",
                "WEAK_HEDGE",
                path,
                line_no,
                '"if in doubt" overtriggers its fallback; state the default flat or give a checkable trigger',
            )
        )


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Lint agent prompts, skills, and AGENTS.md files.")
    parser.add_argument("paths", nargs="*", default=["."], help="Package or repo root directories to lint.")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero on warnings as well as errors.")
    args = parser.parse_args(argv)

    total_errors = 0
    total_warns = 0

    for raw in args.paths:
        root = Path(raw).resolve()
        findings, stats = lint_package(root)
        errors = sum(1 for f in findings if f.severity == "ERROR")
        warns = sum(1 for f in findings if f.severity == "WARN")
        total_errors += errors
        total_warns += warns

        print(
            f"=== {root.name} === "
            f"(agents={stats['agents']}, skills={stats['skills']}, "
            f"AGENTS.md={stats['agents_md']}, desc_chars={stats['desc_chars']}/{CODEX_DESC_BUDGET}, "
            f"errors={errors}, warns={warns})"
        )
        for f in findings:
            print("  " + f.format(root))

    if total_errors > 0 or (args.strict and total_warns > 0):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

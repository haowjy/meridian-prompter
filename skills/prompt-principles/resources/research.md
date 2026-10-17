# Research Backing

## Direct Empirical Support

| Finding | Source |
|---------|--------|
| Position matters (primacy/recency) | "Lost in the Middle" (Liu et al., 2023) |
| Prompt repetition can improve compliance on non-reasoning models | arxiv:2512.14982 |
| Persona prompts help some tasks (alignment, style) and hurt others (reasoning accuracy) | PRISM study (arxiv:2603.18507) |
| Multi-agent orchestrator outperforms single on breadth-first queries in one study | Anthropic multi-agent research (90.2% improvement) |
| Self-reflection without external tools fails | CRITIC framework (arxiv:2305.11738) |
| Conditional constraints are met 15 to 21 points less often than plain ones (Claude 4 Sonnet: 83.6% vs 62.2%) | AgentIF (NeurIPS 2025) |
| Adding requirements doesn't reliably help: they compete; underspecified prompts regress about twice as often across model or prompt changes | Yang et al. 2025, "What Prompts Don't Say" (arxiv:2505.13360) |
| Following several instructions at once collapses past five or six simultaneous constraints (preprint) | Vasileva 2026, "LLMs Can Follow Instructions, But Not Many at Once" (arxiv:2608.12426) |
| Curated skills add 16 points on average, but 16 of 84 tasks got worse, and self-generated skills gave no average benefit | Li et al. 2026, SkillsBench (arxiv:2602.12670v1; later versions report different numbers) |
| One level of disclosure helps; a second routing level never helped in aggregate and sometimes hurt (long-document QA) | He et al. 2026 (arxiv:2607.17598) |
| Multi-agent failures cluster in system design issues, inter-agent misalignment, and task verification (over 1,600 traces, 7 frameworks) | Cemri et al. 2025, MAST (arxiv:2503.13657) |
| An AGENTS.md file cut median runtime 29% and output tokens 17% with comparable completion (10 repos, 124 PRs) | Lulla et al. 2026 (arxiv:2601.20404) |

## Documented Guidance And Operational Practice

| Finding | Source |
|---------|--------|
| XML tags and clear structure are recommended over unstructured prompts | Anthropic prompt engineering docs |
| "If in doubt, use [tool]" causes overtriggering | Anthropic Claude prompting guidance |

## Practitioner Collections

| Practice | Source |
|---|---|
| Pointer wording decides reach; disclose by branch; completion criteria (clarity, demand); environment restated in a doc is a cache; sediment | Matt Pocock, `writing-for-agents` and `SKILL-MECHANICS.md` (github.com/mattpocock/skills, 2026) |
| Accept a change only for an observed failure in a real session | Matt Pocock, `SCOPE.md` |
| Blind evaluation: organic prompts, sanitized names, a judge on another family, grading from transcripts; edit skills in their own change | Cursor pstack, `playbooks/eval.md` and `docs/guide/09-make-it-yours.md` (github.com/cursor/plugins) |
| Encode lessons in structure: architecture, types or lint, tests, then docs; proceed on reversible work | Cursor pstack, `principle-encode-lessons-in-structure`, `principle-never-block-on-the-human` |
| Trigger tests with positive and near-miss queries against a no-skill baseline; prescription by fragility | Anthropic skill-authoring best practices and `skill-creator` (2025-2026) |

## Surveys for Deeper Reading

- Large Language Model Agent: A Survey on Methodology, Applications and Challenges (arxiv:2503.21460)
- Large Language Model based Multi-Agents: A Survey of Progress and Challenges (arxiv:2402.01680)
- Understanding the Planning of LLM Agents: A Survey (arxiv:2402.02716)
- Anthropic: Building Effective Agents (anthropic.com/research/building-effective-agents)

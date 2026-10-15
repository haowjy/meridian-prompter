# Research Backing

Research citations for key principles, grouped by evidence strength.

## Direct Empirical Support

| Finding | Source |
|---------|--------|
| Position matters (primacy/recency) | "Lost in the Middle" (Liu et al., 2023) |
| Prompt repetition can improve compliance on non-reasoning models | arxiv:2512.14982 |
| Persona prompting hurts reasoning | PRISM study (arxiv:2603.18507) |
| RLHF models follow instructions better than pre-RLHF | InstructGPT (arxiv:2203.02155) |
| Multi-agent orchestrator outperforms single on breadth-first queries in one study | Anthropic multi-agent research (90.2% improvement) |
| ~2% context retention loss per handoff step | Multi-Layered Memory Architectures (arxiv:2603.29194) |
| Self-reflection without external tools fails | CRITIC framework (arxiv:2305.11738) |
| ReAct outperforms pure CoT on multi-hop reasoning | ReAct (arxiv:2210.03629) |
| Conditional constraints are met 15 to 21 points less often than plain ones (Claude 4 Sonnet: 83.6% vs 62.2%) | AgentIF (NeurIPS 2025) |

## Documented Guidance And Operational Practice

| Finding | Source |
|---------|--------|
| XML tags and clear structure are recommended over unstructured prompts | Anthropic prompt engineering docs |
| "If in doubt, use [tool]" causes overtriggering | Anthropic Claude prompting guidance |
| Tool sets above ~20 can degrade selection quality in practice | Agent harness failures research |
| Max iterations around 15-25 are common production guardrails | Multiple production systems documented |

## Key Quotes from Research

On self-critique:
> "Almost every published 'success' of reflection is actually a success of verification. Strip away the external tool:the compiler, the test suite, the search engine:and the gains vanish."

On multi-agent complexity:
> "Default to a single agent and only introduce multi-agent architecture when you have evidence that additional complexity delivers proportional value."

On task decomposition:
> "In most cases, task decomposition has limited impact: if the task is simple, a single agent can solve it; if it is too difficult, multi-agent systems still fail."

On convergence:
> "LLMs are notoriously bad at knowing when to stop:they'll either quit too early or never quit at all."

On loop guards:
> "Loop guardrails are based on external enforcement: the system running the agent, not the agent itself, is ultimately responsible for guaranteeing termination."

On implementation approach:
> "Most successful implementations weren't using complex frameworks but simple, composable patterns."

## Surveys for Deeper Reading

- Large Language Model Agent: A Survey on Methodology, Applications and Challenges (arxiv:2503.21460)
- Large Language Model based Multi-Agents: A Survey of Progress and Challenges (arxiv:2402.01680)
- Understanding the Planning of LLM Agents: A Survey (arxiv:2402.02716)
- Anthropic: Building Effective Agents (anthropic.com/research/building-effective-agents)

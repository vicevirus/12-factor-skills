# 10. Small, Focused Agents

**HumanLayer:** [Factor 10](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-10-small-focused-agents.md) describes agents as focused components inside a larger, mostly deterministic system. Long, complex tasks create longer contexts and increase the risk of the model losing focus. “3–10, maybe 20 steps” describes useful scope, not a runtime constraint; scope may expand as capability permits without losing quality.

**Why / when:** Reconsider a worker that owns many unrelated decisions, tools and histories, or a research task that overfills one context. Narrow responsibilities are easier to understand, test and debug.

**Application pattern (illustrative):** First move predictable retrieval and execution out of an oversized worker into code. If distinct model judgments remain, software can partition a research assignment: a source-finding worker receives one question and search tools, a synthesis worker receives compact findings, and the parent coordinates outputs. Give each worker relevant context/tools and a checkable result; if one bounded model call suffices, keep one.

**Misreading:** A small agent is not automatically necessary for each step: deterministic work stays in code, and the source's illustrative step range is not a hard cap.

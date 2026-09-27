# 4. Tools Are Just Structured Outputs

**HumanLayer:** [Factor 4](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-04-tools-are-structured-outputs.md) models a tool choice as structured output from an LLM. Application code interprets the declared intent and controls the resulting action. A model's chosen “tool” need not map one-to-one to immediate function execution.

**Why / when:** Use this lens when tool abstractions obscure how a model decision becomes an external effect, or when a decision should instead queue work, ask for approval or return a result.

**Application pattern (illustrative):** A typed union `SearchIssues(query) | CreateIssue(issue) | Done(message)` feeds a code-owned dispatcher. One branch searches, another pauses for review, and the last ends the run. Select a structured-output mechanism that works with the chosen model/provider.

**Misreading:** HumanLayer does not prescribe JSON mode over provider tool calling, one schema library, or a direct function invocation for each model output. The structure is the decision interface; code still owns effects.

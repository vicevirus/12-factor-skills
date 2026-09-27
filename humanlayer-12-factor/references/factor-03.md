# 3. Own Your Context Window

**HumanLayer:** [Factor 3](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md) treats the model input—prompt, retrieved data, history, tool results, memory and output instructions—as an engineered interface. It explores custom formats as well as ordinary role messages, and distinguishes stored state from what is passed to the model.

**Why / when:** As runs lengthen, irrelevant or verbose history dilutes attention, consumes tokens and can obscure the next decision. Shape the information the model needs now, with flexibility to change the representation.

**Application pattern (illustrative):** For a release decision, pass the user's target, current eligible tags and a compact record of unresolved blockers; retain full tool logs outside the model input. Filter, summarize or omit resolved errors and unrelated past work. Compare custom formatting with native role messages for the task.

**Misreading:** A thread or event store is not a mandate to dump its full contents into context. XML tags are an example, not required syntax; blindly pre-fetching everything contradicts information density.

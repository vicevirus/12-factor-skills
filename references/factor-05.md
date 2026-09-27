# 5. Unify Execution State and Business State

**HumanLayer:** [Factor 5](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-05-unify-execution-state.md) observes that separate orchestration state (step, wait, retries) and business history (messages, calls, results) can duplicate information. Unify them *as much as possible* when it simplifies recovery. The source explicitly leaves the choice to the application and notes some data cannot go in model context.

**Why / when:** For resumable workflows, avoid two conflicting accounts of what happened and what comes next. A coherent thread can make serialization, inspection, recovery and forking easier.

**Application pattern (illustrative):** Persist a workflow record containing relevant events and a pending approval; derive “waiting for approval” from that record where practical. Keep secrets, session identifiers or operational metadata outside model-visible context; construct the model input separately.

**Misreading:** “All state must live in an event list,” “stored state equals model context,” and “separate state is forbidden” all strengthen the source beyond its conditional advice. Retain separate execution state when it genuinely reduces complexity.

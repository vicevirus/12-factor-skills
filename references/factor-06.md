# 6. Launch/Pause/Resume with Simple APIs

**HumanLayer:** [Factor 6](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-06-launch-pause-resume.md) asks for simple ways for users, software or other agents to launch, query, resume and stop an agent. Orchestrating code should be able to pause for a long-running operation and resume from an external event. The source particularly highlights pausing between tool selection and execution.

**Why / when:** A workflow waiting for a human or webhook should not need to keep an in-memory model loop alive, restart the whole task, or execute a consequential action before review.

**Application pattern (illustrative):** Expose `start(input) -> run_id`, `status(run_id)`, and `resume(run_id, event)` around durable run state; persist a proposed operation, pause, then process the approval event before executing it. Use an existing orchestrator if it supports the needed pause boundary.

**Misreading:** Not every single-call LLM feature needs a durable agent API. A framework's generic “pause” is insufficient for a workflow that must inspect a selected tool call *before* invocation.

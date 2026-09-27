# 8. Own Your Control Flow

**HumanLayer:** [Factor 8](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-08-own-your-control-flow.md) asks application code to shape transitions for its own use case: fetch and continue, pause for clarification or approval, compact context, wait for events, and optionally add caching, tracing or rate limiting. The shown `while` loop is an example.

**Why / when:** Model-selected intents can require different execution semantics, especially when an operation is long-running or should be reviewed before it runs. Opaque framework loops can hide the crucial pause boundary.

**Application pattern (illustrative):** A deployment workflow routes a proposed tag to an approval wait, fetches status deterministically, and invokes deployment only on the approved path. A pipeline, DAG, router, orchestrator-worker design, single call or bounded loop can each express the needed transitions.

**Misreading:** Owning control flow is not a requirement to implement `while true`, nor a requirement to rebuild every orchestration primitive. Retain a framework when the important transitions remain inspectable and controllable.

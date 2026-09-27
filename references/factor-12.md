# 12. Make Your Agent a Stateless Reducer

**HumanLayer:** [Factor 12](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-12-stateless-reducer.md) names the stateless-reducer framing and illustrates it mainly with diagrams; the accompanying text calls it “mostly just for fun.” Read it alongside [Factor 5](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-05-unify-execution-state.md) and [Factor 6](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-06-launch-pause-resume.md), rather than treating it as a detailed persistence specification.

**Why / when:** For a resumable workflow, it is useful to ask whether the next model decision can be reconstructed from explicit state and a new event instead of hidden in-memory conversational state.

**Application pattern (interpretation, not a source mandate):** Model the boundary as `next(state, incoming_event) -> decision`; store what is needed to resume, render a selected part of it into context, then let code enact the decision. Real execution can still perform I/O and hold application-specific state.

**Misreading:** HumanLayer does not require a mathematically pure function, a complete event-sourcing architecture, or that every byte of operational state be included in a model prompt.

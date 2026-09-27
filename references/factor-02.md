# 2. Own Your Prompts

**HumanLayer:** [Factor 2](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-02-own-your-prompts.md) calls for treating model instructions as first-class code, with control over the actual text rather than only a framework's `role`, `goal`, or `personality` knobs. The source explicitly allows a prompt tool, a framework or manual templates when the developer can still tune the prompt.

**Why / when:** Inspect the effective instructions when an LLM decision behaves unexpectedly, a prompt needs iteration, or a library assembles hidden instructions. Control enables targeted tests and experiments.

**Application pattern (illustrative):** Keep the task prompt and its dynamic fields in a versioned template; inspect the rendered messages at the model boundary, then change instructions without reverse-engineering an opaque agent wrapper. Use the existing library's templating if it exposes the emitted prompt.

**Misreading:** Ownership does not require hand-writing every API call, adopting a particular prompt language, or replacing an existing framework. HumanLayer's BAML snippet is an example, not a dependency.

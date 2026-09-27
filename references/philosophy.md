# Philosophy: software first, model judgment where useful

**HumanLayer:** [README](https://github.com/humanlayer/12-factor-agents/blob/main/README.md) describes strong LLM products as mostly deterministic code with LLM steps at carefully chosen points. It recommends incorporating small, modular agent concepts into existing products rather than treating a framework or an open-ended tool loop as the entire product. Its discussion of frameworks is about retaining the ability to tune important behavior, not banning libraries.

**Why:** Code can reliably execute known transitions; the model adds value when language interpretation or uncertain decisions determine the next step. The useful boundary often looks like code preparing relevant information, a bounded agent invocation yielding structured output, and code acting on that output. A bounded invocation, pipeline, or focused worker can each be appropriate; the invocation may include multiple model requests.

**When designing:** Mark each proposed model invocation and ask what decision it makes that code cannot reliably make. Trace which application code builds its prompt and context, interprets its output, controls its effects and decides whether to call it again. In a review, treat factors as lenses for real problems, not a uniform compliance checklist.

**Application pattern (illustrative):** A ticket workflow deterministically loads category definitions, asks the model for a category only if rules cannot decide, parses the response, and routes the ticket in code. No autonomous loop is needed.

**Misreading:** More tools, more history, more model steps or a framework rewrite are not inherently improvements. Retain useful existing abstractions when prompts, context and control remain adjustable.

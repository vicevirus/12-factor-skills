# 7. Contact Humans with Tool Calls

**HumanLayer:** [Factor 7](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-07-contact-humans-with-tools.md) treats asking for human input, clarification or approval as a structured intent, just like other tool decisions. Persist the request, contact the person, then accept a later reply into the workflow. The source suggests experimenting with a consistently structured output format; it makes no performance guarantee.

**Why / when:** External or long-running workflows need an explicit bridge between model choice and human response, especially before a consequential operation.

**Application pattern (illustrative):** Model outputs `request_human_input(question, context, options)`; code saves the pending request and run identifier, notifies a user, and on a webhook records the reply and resumes. A human response can enter model context in a deliberately shaped form.

**Misreading:** “Contact human” is neither free text that implicitly completes the workflow nor a guarantee that a specific model-output encoding improves accuracy. Human decisions and side effects still pass through application control.

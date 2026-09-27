# 1. Natural Language to Tool Calls

**HumanLayer:** [Factor 1](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-01-natural-language-to-tool-calls.md) demonstrates translating a request into a structured description of an action and letting deterministic code handle it. The atomic translation itself is useful; feeding the result back into a model loop is optional.

**Why / when:** Use model interpretation when a person expresses an intent in natural language and software needs explicit parameters before it can act. This separates an uncertain interpretation from a reliable execution path.

**Application pattern (illustrative):** Turn “create a payment link for $750” into `{"intent":"create_payment_link","amount":750,"customer_id":"..."}`; have application code resolve any unknown IDs and call the payment service. For a single extraction, stop after the deterministic handler. If the model needs to choose among customers, supply or retrieve those candidates deliberately.

**Misreading:** A tool call is not a command the model executes itself, nor does this factor imply a perpetual autonomous agent or that a tool result must be sent back for another model turn.

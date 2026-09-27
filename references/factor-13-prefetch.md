# 13. Pre-fetch All the Context You Might Need (appendix)

**HumanLayer:** [Appendix 13](https://github.com/humanlayer/12-factor-agents/blob/main/content/appendix-13-pre-fetch.md) says that if the model is highly likely to call a tool for data, application code can call it before the model instead of spending a model turn asking to fetch it. Its deployment example fetches git tags first; the model reasons over the result. The material can enter via a dedicated prompt field or a thread event.

**Why / when:** Predictable data retrieval is software work; skipping the needless tool-selection round trip leaves the model to decide how to use the information.

**Application pattern (illustrative):** For a release-selection request, load the current, relevant tags deterministically and pass a compact list to the decision prompt. Fetch incident details later if their need depends on the chosen release or model reasoning.

**Misreading:** “All the context you might need” does not mean loading all repositories, logs or available tool outputs. Pre-fetch cheap, predictable, relevant material in a form that fits [Factor 3's context engineering](factor-03.md); keep genuinely contingent retrieval dynamic.

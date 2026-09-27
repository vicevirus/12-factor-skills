# 11. Trigger From Anywhere, Meet Users Where They Are

**HumanLayer:** [Factor 11](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-11-trigger-from-anywhere.md) describes launching from user channels such as Slack, email or SMS, and non-human triggers such as events, cron or outages; replies can travel through those channels too. Combined with pause/resume and human contact, this enables work begun outside an interactive chat.

**Why / when:** When a workflow starts from a scheduler or operational event, a chat UI need not be the only entrypoint; the agent may later need help or approval from a person.

**Application pattern (illustrative):** Normalize a Slack message, webhook or scheduled job into an application request containing source and reply destination. Use the same underlying workflow interface and send the eventual response through the appropriate channel.

**Misreading:** “Trigger anywhere” is capability for the channels the product needs, not a requirement to implement every possible integration. A channel adapter should not silently determine model context or workflow policy.

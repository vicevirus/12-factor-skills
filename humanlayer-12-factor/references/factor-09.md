# 9. Compact Errors into Context Window

**HumanLayer:** [Factor 9](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-09-compact-errors.md) feeds useful tool failure information back to the model when it can change the next attempt. It warns that repeated failures can spin; a tool-specific counter around three attempts is an example, and the source explicitly allows other limits or escalation behavior. Error representation and retained history are adjustable.

**Why / when:** A recoverable failure can inform the next decision without flooding context with full traces or repeatedly making the same broken call.

**Application pattern (illustrative):** Record `deploy failed: service unavailable; target=staging` for the next decision; keep the complete trace in ordinary diagnostics. Bound attempts according to the operation, then stop or ask a human if the same failure persists. Remove resolved errors from model-visible context when they cease to help.

**Misreading:** Do not turn “~3” into a universal retry limit, or assume the model should retry every failure. A raw stack dump can crowd out relevant context.

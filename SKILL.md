---
name: humanlayer-12-factor
description: Use when designing or implementing AI/LLM applications, agent harnesses, tool-calling workflows, context management, orchestration, state and recovery, or multi-agent systems; also when reviewing or refactoring agent architecture, debugging agent drift or context dilution, or deciding whether an agent is needed rather than deterministic software.
---

# HumanLayer 12-Factor Agents

Build LLM-powered applications as mostly deterministic software, inserting model reasoning where it earns its place. This skill applies to architecture decisions during implementation and review, not to ordinary non-LLM programming. [HumanLayer's README](https://github.com/humanlayer/12-factor-agents/blob/main/README.md) is the methodology source; [philosophy](references/philosophy.md) explains the architectural choice.

## Work the boundary

1. Identify what genuinely requires model judgment. For classification, a focused agent invocation can be one bounded application step without being one provider request: it may make multiple model requests or relevant tool calls internally. If rules suffice, use code. Keep predictable routing and execution in application code.
2. Shape the model boundary: owned prompt, relevant constructed context, explicit structured decision, deterministic interpretation. Choose the smallest useful scope and tools. For predictable data, fetch before the model; retrieve contingent data when reasoning reveals the need.
3. For workflows needing multiple steps, choose suitable control flow (pipeline, routing, DAG, workers, bounded loop). Make state, pauses, human input, errors and resumption understandable at the actual boundaries. Keep the framework already in use if it permits meaningful control over prompts, context, state, interfaces and flow. When implementing, trace the real entrypoint through context construction, model decision and deterministic handler; change that path and run it to observe the selected context, resulting action and any pause or effect.
4. Review the resulting architecture as tradeoffs, not a checklist: where is model reasoning valuable, what context reaches it, what does code execute, and how does a run recover? Separate each HumanLayer principle from an application-specific recommendation; derive any tool, step or retry limit from the application's needs rather than from illustrative numbers in the source.

## Factor map — load only relevant references

| Design question | Reference |
| --- | --- |
| 1. Translate natural language into a tool decision? | [Natural Language to Tool Calls](references/factor-01.md) |
| 2. Control the exact instructions sent? | [Own Your Prompts](references/factor-02.md) |
| 3. Select and format the model's actual input? | [Own Your Context Window](references/factor-03.md) |
| 4. Interpret tools as structured model output? | [Tools Are Just Structured Outputs](references/factor-04.md) |
| 5. Simplify execution and business state? | [Unify Execution State and Business State](references/factor-05.md) |
| 6. Launch, pause or resume a run? | [Launch/Pause/Resume with Simple APIs](references/factor-06.md) |
| 7. Ask a human for input or approval? | [Contact Humans with Tool Calls](references/factor-07.md) |
| 8. Decide branching, waits or orchestration? | [Own Your Control Flow](references/factor-08.md) |
| 9. Recover from tool failure without error spin? | [Compact Errors into Context Window](references/factor-09.md) |
| 10. Scope a large agent or several workers? | [Small, Focused Agents](references/factor-10.md) |
| 11. Support other entrypoints or reply channels? | [Trigger From Anywhere](references/factor-11.md) |
| 12. Reason about run transition from state and input? | [Make Your Agent a Stateless Reducer](references/factor-12.md) |
| 13. Predictably need data before a model call? | [Pre-fetch Context (appendix)](references/factor-13-prefetch.md) |

When reviewing an existing system, use these questions to find the *relevant* tensions; propose local changes supported by the application, rather than implementing all thirteen patterns by default. In each factor reference, **HumanLayer** marks source-backed guidance and **Application pattern** marks an illustrative choice, not a source requirement.

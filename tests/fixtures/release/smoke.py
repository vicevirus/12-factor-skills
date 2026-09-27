from app import run_release


def scenario(decisions, approved):
    calls = []
    contexts = []
    steps = iter(decisions)

    def decide(context):
        contexts.append(dict(context))
        return next(steps)

    result = run_release(
        "ship backend", lambda: calls.append("tags") or ["v1", "v2"],
        lambda: calls.append("logs") or "large incident logs", decide,
        lambda tag: calls.append("deploy:" + tag) or "deployed",
        lambda tag: calls.append("approve:" + tag) or approved,
    )
    return result, calls, contexts


result, calls, contexts = scenario([{"intent": "deploy", "tag": "v1"}], False)
assert result == "rejected"
assert calls == ["tags", "approve:v1"], calls
assert contexts[0]["tags"] == ["v1", "v2"]
assert "incident_logs" not in contexts[0]

result, calls, contexts = scenario([
    {"intent": "inspect_incidents"}, {"intent": "deploy", "tag": "v2"}
], True)
assert result == "deployed"
assert calls == ["tags", "logs", "approve:v2", "deploy:v2"], calls
assert "incident_logs" not in contexts[0]
assert contexts[1]["incident_logs"] == "large incident logs"
print("PASS release: eager tags, conditional incidents, approval before deployment")

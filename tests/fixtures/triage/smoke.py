from app import triage


def scenario(category):
    calls = []
    decisions = []
    categories = ["billing", "technical"]

    def ask_model(context, tools):
        decisions.append((dict(context), tuple(tools)))
        return {"intent": "classify", "category": category}

    def load_categories():
        calls.append("categories")
        return categories

    def load_history():
        calls.append("history")
        return "large unrelated thread"

    def save(value):
        calls.append("save:" + value)

    def route(value):
        calls.append("route:" + value)

    def run():
        return triage("Invoice question", load_categories, load_history, ask_model, save, route)

    return run, calls, decisions


run, calls, decisions = scenario("billing")
assert run() == "billing"
assert calls == ["categories", "save:billing", "route:billing"], calls
assert len(decisions) == 1, decisions
context, tools = decisions[0]
assert context["categories"] == ["billing", "technical"]
assert "history" not in context
assert not {"load_categories", "load_history", "save_record", "route_email"}.intersection(tools)

run, calls, decisions = scenario("nonexistent")
try:
    run()
except ValueError:
    pass
else:
    raise AssertionError("unknown category was accepted")
assert calls == ["categories"], calls
print("PASS triage: one bounded choice, relevant context, code-owned routing")

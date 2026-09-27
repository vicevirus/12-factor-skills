from app import run_job


long_error = "temporary outage: " + "X" * 5000


def exhausted(limit):
    targets = []

    def execute(target):
        targets.append(target)
        raise RuntimeError(long_error)

    result = run_job("check", lambda _: {"intent": "run", "target": "primary"}, execute, limit)
    assert result == "failed"
    assert len(targets) == limit, targets


exhausted(1)
exhausted(2)

targets = []
contexts = []


def decide(context):
    contexts.append(str(context))
    if len(contexts) == 1:
        return {"intent": "run", "target": "primary"}
    assert "temporary outage" in contexts[-1], contexts[-1]
    assert len(contexts[-1]) < 500, len(contexts[-1])
    return {"intent": "run", "target": "secondary"}


def execute(target):
    targets.append(target)
    if target == "primary":
        raise RuntimeError(long_error)
    return "ok"


assert run_job("check", decide, execute, 2) == "ok"
assert targets == ["primary", "secondary"], targets
assert len(contexts) == 2
print("PASS errors: useful compact failure, recovery, caller-bounded attempts")

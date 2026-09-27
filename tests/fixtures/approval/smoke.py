from app import start, resume


def scenario():
    state = {}
    calls = []

    def save(*args):
        if len(args) == 1:
            run_id = "run-1"
            state[run_id] = dict(args[0])
            return run_id
        state[args[0]] = dict(args[1])

    def load(run_id):
        return dict(state[run_id])

    def deploy(tag):
        calls.append("deploy:" + tag)

    def notify(run_id, tag):
        calls.append("notify:" + run_id + ":" + tag)

    run_id = start("ship", lambda _: {"intent": "deploy", "tag": "v1"}, save, notify, deploy)
    assert run_id == "run-1"
    assert state[run_id] == {"status": "waiting", "tag": "v1"}, state
    assert calls == ["notify:run-1:v1"], calls
    return run_id, state, calls, load, save, deploy


run_id, state, calls, load, save, deploy = scenario()
assert resume(run_id, False, load, save, deploy) == "declined"
assert calls == ["notify:run-1:v1"], calls
assert state[run_id]["status"] == "declined"

run_id, state, calls, load, save, deploy = scenario()
assert resume(run_id, True, load, save, deploy) == "done"
assert calls == ["notify:run-1:v1", "deploy:v1"], calls
assert resume(run_id, True, load, save, deploy) == "done"
assert calls == ["notify:run-1:v1", "deploy:v1"], calls
print("PASS approval: durable wait, rejection, resume, no duplicate deployment")

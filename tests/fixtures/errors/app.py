import traceback


def run_job(request, decide, execute, limit):
    """Let the model choose a target for one short operation."""
    context = {"request": request, "errors": []}
    attempts = 0
    while True:
        action = decide(context)
        if action["intent"] == "done":
            return action["message"]
        if action["intent"] != "run":
            raise ValueError("unknown intent")
        try:
            return execute(action["target"])
        except Exception:
            attempts += 1
            context["errors"].append(traceback.format_exc())
            if attempts >= 3:
                return "failed"

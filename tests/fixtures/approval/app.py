def start(request, decide, save, notify, deploy):
    """Start a run and return its identifier."""
    action = decide(request)
    if action["intent"] == "deploy":
        deploy(action["tag"])
        run_id = save({"status": "waiting", "tag": action["tag"]})
        notify(run_id, action["tag"])
        return run_id
    return save({"status": "done"})


def resume(run_id, approved, load, save, deploy):
    """Process a human reply for a pending run."""
    run = load(run_id)
    if approved:
        deploy(run["tag"])
        run["status"] = "done"
    else:
        run["status"] = "declined"
    save(run_id, run)
    return run["status"]

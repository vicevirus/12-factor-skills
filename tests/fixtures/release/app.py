def run_release(request, list_tags, incident_logs, decide, deploy, approve):
    """Choose a release and execute the selected action."""
    context = {"request": request, "incident_logs": incident_logs()}
    while True:
        action = decide(context)
        if action["intent"] == "list_tags":
            context["tags"] = list_tags()
        elif action["intent"] == "inspect_incidents":
            context["incident_logs"] = incident_logs()
        elif action["intent"] == "deploy":
            result = deploy(action["tag"])
            if not approve(action["tag"]):
                return "rejected"
            return result
        elif action["intent"] == "done":
            return action["message"]
        else:
            raise ValueError("unknown intent")

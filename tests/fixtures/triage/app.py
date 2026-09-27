def triage(email, load_categories, load_history, ask_model, save, route):
    """Classify and route a message."""
    context = {"email": email, "history": load_history()}
    tools = ("load_categories", "load_history", "save_record", "route_email")
    while True:
        decision = ask_model(context, tools)
        if decision["intent"] == "load_categories":
            context["categories"] = load_categories()
        elif decision["intent"] == "load_history":
            context["history"] = load_history()
        elif decision["intent"] == "save_record":
            save(decision["category"])
        elif decision["intent"] == "route_email":
            route(decision["category"])
        elif decision["intent"] == "done":
            return decision["message"]
        else:
            raise ValueError("unknown intent")

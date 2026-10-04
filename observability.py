def observe_decide_act():
    log = []

    # Step 1: Observe
    state = {"temperature": 30, "rain": False}
    log.append({
        "step": 1,
        "action": "observe",
        "state": state.copy()
    })

    # Step 2: Decide
    if state["rain"]:
        decision = "Carry an umbrella"
    else:
        decision = "No umbrella needed"

    log.append({
        "step": 2,
        "action": "decide",
        "decision": decision
    })

    # Step 3: Act
    result = f"Action: {decision}"
    log.append({
        "step": 3,
        "action": "act",
        "result": result
    })

    # Return the complete observability log
    return log


# Run the process
full_log = observe_decide_act()

# Display full log
for entry in full_log:
    print(entry)
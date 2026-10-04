def observe_decide_act():
    max_iters = 10

    # State dictionary
    state = {
        "done": False,
        "steps": 0
    }

    while not state["done"] and state["steps"] < max_iters:

        # Observe
        print("Observing...")

        # Decide
        print("Deciding...")

        # Act
        print("Taking action...")

        # Update state
        state["steps"] += 1

        # Example condition for completion
        if state["steps"] == 5:
            state["done"] = True

    # Return result
    if state["done"]:
        return "success", state
    else:
        return "failure", state


result, state = observe_decide_act()

print("Result:", result)
print("State:", state)
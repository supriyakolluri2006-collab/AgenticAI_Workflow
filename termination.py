def observe_decide_act():
    max_iters = 10

    state = {
        "done": False,
        "steps": 0
    }

    for i in range(max_iters):
        state["steps"] += 1

        # Observe
        observation = i + 1

        # Decide
        if observation >= 5:
            decision = "success"
        else:
            decision = "continue"

        # Act
        if decision == "success":
            state["done"] = True
            return "success", state

        print("Step:", state["steps"])
        print("Status: continue")

    # Termination after maximum iterations
    state["done"] = True
    return "failure", state


# Run the loop
status, state = observe_decide_act()

print("\nFinal Status:", status)
print("State:", state)
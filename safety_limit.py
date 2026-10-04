def observe_decide_act():
    max_iters = 10

    for i in range(max_iters):
        print("Iteration:", i + 1)

        # Observe
        observation = "task not completed"

        # Decide
        if observation == "task completed":
            return "success"

        # Act
        print("Taking action...")

    # If maximum iterations are exceeded
    return "failure"


result = observe_decide_act()
print("Result:", result)
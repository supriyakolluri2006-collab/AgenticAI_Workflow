def agent_loop(inputs):
    for i in range(3):
        print(f"\n--- Iteration {i + 1} ---")

        # Observe
        observation = inputs[i]
        print("Observe:", observation)

        # Decide
        if observation > 50:
            decision = "High"
        else:
            decision = "Low"
        print("Decide:", decision)

        # Evaluate
        if decision == "High":
            evaluation = "Take action"
        else:
            evaluation = "No major action needed"
        print("Evaluate:", evaluation)

        # Act
        if evaluation == "Take action":
            action = "Reduce the value"
        else:
            action = "Keep the value"

        print("Act:", action)


# Input values
inputs = [40, 75, 30]

# Run agent loop
agent_loop(inputs)
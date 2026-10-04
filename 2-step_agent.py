# 2-Step Agent Loop

state = {"step": 0, "status": "start"}

for i in range(2):
    state["step"] += 1

    if state["step"] == 1:
        action = "Observe"
        result = "Environment checked"
    else:
        action = "Act"
        result = "Action completed"

    print("Step:", state["step"])
    print("Action:", action)
    print("Result:", result)
    print()

print("Final State:", state)
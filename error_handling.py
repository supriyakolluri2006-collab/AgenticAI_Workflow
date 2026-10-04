def perform_action(action):
    valid_actions = ["observe", "decide", "act"]

    if action not in valid_actions:
        return {
            "status": "error",
            "message": "Invalid action",
            "action": action
        }

    if action == "observe":
        return {
            "status": "success",
            "message": "Observation completed"
        }

    elif action == "decide":
        return {
            "status": "success",
            "message": "Decision completed"
        }

    elif action == "act":
        return {
            "status": "success",
            "message": "Action completed"
        }


# Test with a valid action
print(perform_action("observe"))

# Test with an invalid action
print(perform_action("jump"))
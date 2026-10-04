def temperature_agent(temperature):
    if temperature < 100:
        return "Cool"
    elif temperature > 100:
        return "Idle"
    else:
        return "Temperature is exactly 100"


# Example
temperature = float(input("Enter temperature: "))

action = temperature_agent(temperature)
print("Agent action:", action)
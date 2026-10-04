def temperature_agent(temperature):
    goal = 72

    if temperature > goal:
        return "Cooling"
    elif temperature < goal:
        return "Heating"
    else:
        return "Goal reached: Temperature is 72°C"


temperature = float(input("Enter current temperature: "))

while temperature != 72:
    action = temperature_agent(temperature)
    print("Agent action:", action)

    if temperature > 72:
        temperature -= 1
    elif temperature < 72:
        temperature += 1

print("Goal reached: Temperature is 72°C")
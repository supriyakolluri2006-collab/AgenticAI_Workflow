# Debugging: Fix loop missing increment

i = 0

while i < 5:
    print("Iteration:", i)
    i += 1   # Fixed: increment added

print("Loop completed successfully")
def hundred_doors():
    doors = [False] * 100  # False means closed, True means open
    for step in range(1, 101):
        for i in range(step - 1, 100, step):
            doors[i] = not doors[i]
    return [i + 1 for i, open in enumerate(doors) if open]

# Output
print("Open doors: ", hundred_doors())

def vehicle_of_wheels(V: int, W: int) -> tuple:
    # Looping through the possible number of bicycles
    for bicycles in range(V + 1):
        # Calculating the number of tricycles
        tricycles = V - bicycles
        # Checking if the total wheels match the given number
        if 2 * bicycles + 3 * tricycles == W:
            return (bicycles, tricycles)
    return None

# Input
vehicles = int(input("Enter the total number of vehicles: "))
wheels = int(input("Enter the total number of wheels: "))

# Output
result = vehicle_of_wheels(vehicles, wheels)
if result:
    bicycles, tricycles = result
    print(f"Bicycles: {bicycles}, Tricycles: {tricycles}")
else:
    print("No solution found.")

def eight_cell_colony(days):
    colony = [0, 1, 1, 0, 1, 1, 1, 0]
    for _ in range(days):
        new_colony = [0] * 8
        for i in range(1, 7):
            new_colony[i] = 1 if colony[i-1] != colony[i+1] else 0
        colony = new_colony
    return colony

print(eight_cell_colony(3))  # Example output after 3 days

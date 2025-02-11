def snake_pattern(n):
    for i in range(n):
        row = range(i * n + 1, (i + 1) * n + 1)
        print(" ".join(map(str, row if i % 2 == 0 else reversed(row))))

# Input
n = int(input("Enter a number: "))

# Output
snake_pattern(n)

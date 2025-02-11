def inner_reducing_pattern(n):
    for i in range(n, 0, -1):
        print(" ".join(str(j) for j in range(1, i + 1)))

# Input
n = int(input("Enter a number: "))

# Output
inner_reducing_pattern(n)

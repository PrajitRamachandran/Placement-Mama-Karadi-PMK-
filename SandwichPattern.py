def sandwich_pattern(n):
    for i in range(1, n+1):
        print(" ".join(map(str, range(1, i+1))) + " " + " ".join(map(str, range(i-1, 0, -1))))

# Input
n = int(input("Enter a number: "))

# Output
sandwich_pattern(n)
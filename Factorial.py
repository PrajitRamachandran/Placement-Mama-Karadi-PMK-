def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

# Input
n = int(input("Enter a number: "))

# Output
print("Factorial of", n, "is:", factorial(n))

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# Input
n = int(input("Enter the number of terms: "))

# Output
print("Fibonacci series:", end=" ")
fibonacci(n)

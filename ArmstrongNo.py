def is_armstrong(n):
    return n == sum(int(digit) ** len(str(n)) for digit in str(n))

# Input
n = int(input("Enter a number: "))

# Output
print(n, "is an Armstrong number:", is_armstrong(n))

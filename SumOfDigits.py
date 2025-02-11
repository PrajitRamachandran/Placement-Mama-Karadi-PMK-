def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Input
n = int(input("Enter a number: "))

# Output
print("Sum of digits of", n, "is:", sum_of_digits(n))

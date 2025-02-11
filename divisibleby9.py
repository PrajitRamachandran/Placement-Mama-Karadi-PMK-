def is_divisible_by_9(n):
    return n % 9 == 0

# Input
num = int(input("Enter a number: "))

# Output
print(f"Is {num} divisible by 9? {is_divisible_by_9(num)}")

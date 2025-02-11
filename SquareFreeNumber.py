def is_square_free(n):
    i = 2
    while i * i <= n:
        if n % (i * i) == 0:
            return False
        i += 1
    return True

# Input
num = int(input("Enter a number: "))

# Output
print(f"Is {num} a square-free number? {is_square_free(num)}")

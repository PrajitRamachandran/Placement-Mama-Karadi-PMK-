def is_perfect_number(num):
    return sum_of_proper_divisors(num) == num

print(is_perfect_number(28))  # True
print(is_perfect_number(12))  # False


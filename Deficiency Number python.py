def is_deficient_number(num):
    return sum_of_proper_divisors(num) < num

print(is_deficient_number(8))  # True
print(is_deficient_number(12))  # False
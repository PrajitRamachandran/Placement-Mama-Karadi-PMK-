def is_neon_number(num):
    squared_sum = sum(int(d) for d in str(num * num))
    return squared_sum == num

print(is_neon_number(9))  # True
print(is_neon_number(10))  # False

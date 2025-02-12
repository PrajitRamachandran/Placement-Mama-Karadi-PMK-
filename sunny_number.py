def is_sunny_number(num):
    return ((num + 1) ** 0.5) == int((num + 1) ** 0.5)

print(is_sunny_number(3))  # True
print(is_sunny_number(10))  # False

def factors_of_number(num):
    return [i for i in range(1, num + 1) if num % i == 0]

print(factors_of_number(28))  # [1, 2, 4, 7, 14, 28]
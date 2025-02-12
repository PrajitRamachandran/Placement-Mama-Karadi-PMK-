def is_abundant_number(num):
    return sum_of_proper_divisors(num) > num

print(is_abundant_number(12))  # True
print(is_abundant_number(28))  # False
74. Strong Number
python
def is_strong_number(num):
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)

    return num == sum(factorial(int(digit)) for digit in str(num))

print(is_strong_number(145))  # True
print(is_strong_number(123))  # False

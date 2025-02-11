def is_coprime(a, b):
    return gcd(a, b) == 1

print(is_coprime(15, 28))  # True
print(is_coprime(12, 18))  # False
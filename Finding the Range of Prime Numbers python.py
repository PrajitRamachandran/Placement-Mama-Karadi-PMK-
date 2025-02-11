def prime_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

print(prime_range(10, 50))  # [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
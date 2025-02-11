def previous_prime(num):
    prime_candidate = num - 1
    while prime_candidate > 1 and not is_prime(prime_candidate):
        prime_candidate -= 1
    return prime_candidate

print(previous_prime(29))  # 23
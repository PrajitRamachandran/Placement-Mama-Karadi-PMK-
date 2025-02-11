def next_prime(num):
    prime_candidate = num + 1
    while not is_prime(prime_candidate):
        prime_candidate += 1
    return prime_candidate

print(next_prime(29))  # 31
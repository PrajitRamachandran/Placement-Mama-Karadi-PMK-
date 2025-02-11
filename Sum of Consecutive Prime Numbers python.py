def sum_of_consecutive_primes(n):
    prime_sum = 0
    current_num = 2
    while n > 0:
        if is_prime(current_num):
            prime_sum += current_num
            n -= 1
        current_num += 1
    return prime_sum

print(sum_of_consecutive_primes(5))  # 28 (2 + 3 + 5 + 7 + 11)
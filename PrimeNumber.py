def prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

# Input
n = int(input("Enter a number: "))

# Output
print("Prime numbers up to", n, ":", prime_numbers(n))

def sum_of_divisors(n: int) -> int:
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum

def are_amicable_numbers(a: int, b: int) -> bool:
    if sum_of_divisors(a) == b and sum_of_divisors(b) == a:
        return True
    return False

# Input
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Output
if are_amicable_numbers(a, b):
    print(f"{a} and {b} are amicable numbers.")
else:
    print(f"{a} and {b} are not amicable numbers.")

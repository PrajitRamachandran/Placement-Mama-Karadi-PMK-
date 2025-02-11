def grooming_monkeys(n):
    return "Banana" if n % 2 == 0 else "Coconut"

# Input
num = int(input("Enter a number: "))

# Output
print(f"Monkey gets: {grooming_monkeys(num)}")

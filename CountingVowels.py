def count_vowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")

# Input
s = input("Enter a string: ")

# Output
print("Number of vowels in", s, "is:", count_vowels(s))

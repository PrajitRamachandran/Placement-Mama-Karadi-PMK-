def is_palindrome(s):
    return s == s[::-1]

# Input
s = input("Enter a string: ")

# Output
print(s, "is a palindrome:", is_palindrome(s))

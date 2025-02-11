def rotate_number(n, d, direction="left"):
    str_n = str(n)
    d = d % len(str_n)
    if direction == "left":
        return int(str_n[d:] + str_n[:d])
    else:
        return int(str_n[-d:] + str_n[:-d])

# Input
num = int(input("Enter a number: "))
d = int(input("Enter number of rotations: "))
direction = input("Enter direction (left/right): ")

# Output
print(f"Rotated number: {rotate_number(num, d, direction)}")

def generate_pattern(n):
    pattern = [3, 7, 33, 37, 73, 77]
    for i in range(2, n):
        pattern.append(int(str(pattern[i - 2]) + str(pattern[i - 1])))
    return pattern

print(generate_pattern(8)) 
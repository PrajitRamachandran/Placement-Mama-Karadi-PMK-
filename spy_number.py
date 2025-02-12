def is_spy_number(num):
    digits = [int(d) for d in str(num)]
    return sum(digits) == sum(int(d) for d in str(num)) and \
           prod(digits) == prod(int(d) for d in str(num))

def prod(lst):
    result = 1
    for num in lst:
        result *= num
    return result

print(is_spy_number(1124))  # True
print(is_spy_number(1234))  # False

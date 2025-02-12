def is_adam_number(num):
    def reverse_number(n):
        return int(str(n)[::-1])

    squared_num = num * num
    reversed_num = reverse_number(num)
    squared_reversed_num = reversed_num * reversed_num

    return squared_num == reverse_number(squared_reversed_num)

print(is_adam_number(12))  # True
print(is_adam_number(13))  # False


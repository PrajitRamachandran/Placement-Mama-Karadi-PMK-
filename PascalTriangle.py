def pascal_triangle(rows):
    res = [[1]]
    for _ in range(rows - 1):
        last_row = res[-1]
        new_row = [1] + [last_row[i] + last_row[i+1] for i in range(len(last_row) - 1)] + [1]
        res.append(new_row)
    for row in res:
        print(" ".join(map(str, row)))

# Input
rows = int(input("Enter number of rows for Pascal's Triangle: "))

# Output
pascal_triangle(rows)

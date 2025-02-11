def is_valid(board: list, row: int, col: int, num: int) -> bool:
    # Check if the number already exists in the row or column
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    
    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(board: list) -> bool:
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try numbers 1-9
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Place the number
                        if solve_sudoku(board):  # Recursively attempt to solve
                            return True
                        board[row][col] = 0  # Backtrack if invalid
                return False
    return True  # Puzzle is solved

# Input (example Sudoku board)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the Sudoku
solve_sudoku(board)

# Output
for row in board:
    print(row)

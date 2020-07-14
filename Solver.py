Sudoku = [
    [4, 0, 8, 0, 0, 7, 3, 5, 0],
    [0, 0, 3, 0, 1, 5, 2, 0, 0],
    [0, 6, 5, 0, 3, 0, 0, 4, 0],
    [6, 5, 1, 3, 1, 8, 9, 0, 7],
    [0, 2, 0, 1, 0, 0, 0, 3, 5],
    [0, 4, 9, 0, 7, 2, 0, 0, 0],
    [7, 3, 0, 6, 8, 1, 0, 9, 0],
    [5, 0, 0, 0, 2, 4, 8, 1, 3],
    [0, 0, 0, 9, 5, 0, 6, 7, 4]
]


# Print the sudoku board
def print_sudoku(board):
    for i in range(len(board)):  # Goes through the entire board
        if i % 3 == 0 and i != 0:  # Separate board into 3 "rows"
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:  # Separate board into 3 "columns"
                print(" | ", end="")

            if j == 8:  # Reached end column, print
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# Find "empty" spaces within the board
def empty_space(board):
    for i in range(len(board)):  # Loop through the row
        for j in range(len(board[0])):  # Loop through the column
            if board[i][j] == 0:  # 0 is empty space
                return i, j  # row, col

    return None


# Backtracking through the board

def solver(board):
    empty = empty_space(board)

    #  If solution has been found or not, Base case
    if not empty:
        return True
    else:
        row, col = empty

    for i in range(1, 10):  # Goes through 1 to 9 inclusive and check if correct value
        if correct(board, i, (row, col)):  # If correct, plug in the value in position
            board[row][col] = i

            # Recursively check new board with new value added
            if solver(board):
                return True

            board[row][col] = 0  # Reset element

    return False


def correct(board, num, pos):
    # Check row
    for i in range(len(board[0])):  # loop through every column in row
        if board[pos[0]][i] == num and pos[1] != i:  # Check each element in row if not just insert
            return False

    # Check column
    for i in range(len(board)):  # Loop through every column in row
        if board[i][pos[1]] == num and pos[0] != i:  # Check each element in column if just inserted
            return False

    # Check 3x3 square
    x_pos = pos[1] // 3
    y_pos = pos[0] // 3

    # Loop through 3x3 square
    for i in range(y_pos * 3, y_pos * 3 + 3):  # Go through each element in 3x3 square row wise
        for j in range(x_pos * 3, x_pos * 3 + 3):  # Go through each element 3x3 square column wise
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


print("Initial Sudoku Board")
print_sudoku(Sudoku)
solver(Sudoku)
print("")
print("")
print("Solved Sudoku Board")
print_sudoku(Sudoku)

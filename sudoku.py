''' 
Sudoku Solver 
Written by: Ayaz Vural
'''


board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]



''' Helper Function
    Returns True/False based on if the selected number for our board 
    already exists in a row/column/inner-grid'''
def move_validity(board, row, column, number):
    # if a number is already on a row
    for x in range(9):
        if board[row][x] == number:
            return False
    
    # if a number is already on a column
    for x in range(9):
        if board[x][column] == number:
            return False
    
    # if a number is already in the small grid
    corner_row = row - row % 3
    corner_column = column - column % 3
    for x in range(3):
        for y in range(3):
            if board[corner_row + x][corner_column + y] == number:
                return False
    
    return True
    
    
def sudoku_solver(board, row, column):
    
    if column == 9:
        if row == 8:
            return True
    
        row += 1
        column = 0
    
    if board[row][column] > 0:
        return sudoku_solver(board, row, column + 1)
    
    for number in range(1, 10):
        if move_validity(board, row, column, number):
            board[row][column] = number
            
            if sudoku_solver(board, row, column + 1):
                return True
        
        board[row][column] = 0
    
    return False


if sudoku_solver(board, 0, 0):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

else: 
    print("No Solution")
    
        

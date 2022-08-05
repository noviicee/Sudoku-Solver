unass = 0

def usedInRow(matrix, row, num):
    for col in range(len(matrix)):
        if (matrix[row][col] == num):
            return True
    return False

def usedInCol(matrix, col, num):
    for row in range(len(matrix)):
        if (matrix[row][col] == num):
            return True
    return False

def usedInBox(matrix, boxStartRow, boxStartCol, num):
    for row in range(3):
        for col in range(3):
            if (matrix[row + boxStartRow][col + boxStartCol] == num):
                return True
    return False

def isSafe(matrix, row, col, num):
    return (
        not(usedInRow(matrix, row, num)) and
        not(usedInCol(matrix, col, num)) and 
        not(usedInBox(matrix, row - (row % 3), col - (col % 3), num))
    )

def solveSudoku(matrix):
    row = 0
    col = 0
    checkBlankSpaces = False

    """ verify if sudoku is already solved and if not solved,
    get next "blank" space position """
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if (matrix[row][col] == unass):
                checkBlankSpaces = True
                break
        if (checkBlankSpaces == True):
            break
    # no more "blank" spaces means the puzzle is solved
    if (checkBlankSpaces == False):
        return True

    # try to fill "blank" space with correct num
    for num in range(1, 10):
        """ isSafe checks that num isn't already present 
        in the row, column, or 3x3 box (see below) """
        if (isSafe(matrix, row, col, num)):
            matrix[row][col] = num

            if (solveSudoku(matrix)):
                return True

            """ if num is placed in incorrect position, 
            mark as "blank" again then backtrack with 
            a different num """
            matrix[row][col] = unass
    return False

def printGrid(matrix):
    # print the sudoku grid after solve
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if(col == 3 or col == 6):
                print(" | ", end=" ")
            print(matrix[row][col], end=" ")
        if(row == 2 or row == 5):
            print()
            for i in range(len(matrix[row])):
                print("--", end=" ")
        print()
        
def sudokuSolver(matrix):
    if (solveSudoku(matrix) == True):
        printGrid(matrix)
    else:
        print('NO SOLUTION')


sudokuGrid = [
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

(sudokuSolver(sudokuGrid))

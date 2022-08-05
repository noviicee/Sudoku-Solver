class SudokuSolver:
    def __init__(self) -> None:
        self.UNASSIGNED = 0

    def usedInRow(self, matrix, row, num):
        """Input: The row, and the targeted number.
        Output: True when the number is present in the given column.
        """
        for col in range(len(matrix)):
            if (matrix[row][col] == num):
                return True
        return False

    def usedInCol(self, matrix, col, num):
        """Input: The column, and the targeted number.
        Output: True when the number is present in the given column.
        """
        for row in range(len(matrix)):
            if (matrix[row][col] == num):
                return True
        return False

    def usedInBox(self, matrix, boxStartRow, boxStartCol, num):
        """Input: The starting row and column of a 3 x 3 box, and the targeted number.
        Output: True when the number is present in the box.
        """
        for row in range(3):
            for col in range(3):
                if (matrix[row + boxStartRow][col + boxStartCol] == num):
                    return True
        return False

    def isSafe(self, matrix, row, col, num):
        """Input: Row, a column of the grid, and number to check.
        Output: True, when placing the number at position grid[row, col] is valid.
        """
        # when item not found in col, row and current 3x3 box
        return (
            not(self.usedInRow(matrix, row, num)) and
            not(self.usedInCol(matrix, col, num)) and 
            not(self.usedInBox(matrix, row - (row % 3), col - (col % 3), num))
        )

    def solveSudoku(self, matrix):
        """Input: The unsolved grid of Sudoku.
        Output: Boolean value of if we got a solution.
        """
        row = 0
        col = 0
        checkBlankSpaces = False

        """ verify if sudoku is already solved and if not solved,
        get next "blank" space position """
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if (matrix[row][col] == self.UNASSIGNED):
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
            if (self.isSafe(matrix, row, col, num)):
                matrix[row][col] = num

                if (self.solveSudoku(matrix)):
                    return True

                """ if num is placed in incorrect position, 
                mark as "blank" again then backtrack with 
                a different num """
                matrix[row][col] = self.UNASSIGNED
        return False

    def printGrid(self, matrix):
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
            
    def sudokuSolver(self, matrix):
        if (self.solveSudoku(matrix) == True):
            self.printGrid(matrix)
        else:
            print('NO SOLUTION')

if __name__=="__main__":
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
    obj=SudokuSolver()
    obj.sudokuSolver(sudokuGrid)

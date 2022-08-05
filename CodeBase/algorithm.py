class SudokuSolver:
    def __init__(self) -> None:
        self.grid=grid 
        self.N=9

    def sudokuGrid(self):
        # print the sudoku grid after solve
        for row in range(self.N):
            for col in range(self.N):
                if(col == 3 or col == 6):
                    print(" | ")
                print(grid[row][col], end=" ")

            if(row == 2 or row == 5):
                print()
                for i in range(self.N):
                    print("---")
            print()

    def isPresentInCol(self, col, num) -> bool:
        """Input: The column, and the targeted number.
        Output: True when the number is present in the given column.
        """

        for row in range(self.N):
            if self.grid[row][col]==num:
                return True
        return False

    def isPresentInRow(self, row, num) -> bool:

        """Input: The row, and the targeted number.
        Output: True when the number is present in the given column.
        """
        for column in range(self.N):
            if self.grid[row][column] == num:
                return True
        return False

    def isPresentInBox(self, boxStartRow, boxStartCol, num) -> bool:
        """Input: The starting row and column of a 3 x 3 box, and the targeted number.
        Output: True when the number is present in the box.
        """
        for row in range(boxStartRow, boxStartRow+4):
            for col in range(boxStartCol, boxStartCol+4):
                if self.grid[row][col] == num:
                    return True
        return False

    def findEmptyPlace(self) -> bool:
        """Input: row and column in the grid.
        Output: If the grid[row, col] is empty, then return true, otherwise false.
        """
        for row in range(self.N):
            for col in range(self.N):
                if (self.grid[row][col] ==0):
                    return True
        return False
        
    def isValidPlace(self, row, col, num) ->bool:
        """Input: Row, a column of the grid, and number to check.
        Output: True, when placing the number at position grid[row, col] is valid.
        """
        # when item not found in col, row and current 3x3 box
        if (not(self.isPresentInRow(row, num)) and not(self.isPresentInCol(col, num)) and not(self.isPresentInBox(row-(row%3), col-(col%3), num))):
            return True

    def solveSudoku(self,Grid) ->bool:
        """Input: The unsolved grid of Sudoku.
        Output: Grid after solve.
        """
        if not self.findEmptyPlace():
            return True
        for n in range(1, 10):
            row,col=n,n
            if self.isValidPlace(row, col, n):
                Grid[row][col] = n
                if self.solveSudoku:
                    return True
                Grid[row][col] = 0
        return False

if __name__=="__main__":
    grid = [
   [3, 0, 6, 5, 0, 8, 4, 0, 0],
   [5, 2, 0, 0, 0, 0, 0, 0, 0],
   [0, 8, 7, 0, 0, 0, 0, 3, 1],
   [0, 0, 3, 0, 1, 0, 0, 8, 0],
   [9, 0, 0, 8, 6, 3, 0, 0, 5],
   [0, 5, 0, 0, 9, 0, 6, 0, 0],
   [1, 3, 0, 0, 0, 0, 2, 5, 0],
   [0, 0, 0, 0, 0, 0, 0, 7, 4],
   [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]
    obj=SudokuSolver(grid)
    obj.solveSudoku(grid)
    if (obj.solveSudoku(grid)):
      obj.sudokuGrid()
    else:
      print("No solution exists")


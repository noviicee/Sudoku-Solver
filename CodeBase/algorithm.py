class SudokuSolver:
    def __init__(self, grid) -> None:
        self.grid=grid 

    def isPresentInCol(self, col, num) -> bool:
        """Input: The column, and the targeted number.
        Output: True when the number is present in the given column.
        """

        for row in self.grid:
            if self.grid[row, col]==num:
                return True
        return False

    def isPresentInRow(self, row, num) -> bool:

        """Input: The row, and the targeted number.
        Output: True when the number is present in the given column.
        """
        for column in self.grid:
            if self.grid[row, column] == num:
                return True
        return False

    def isPresentInBox(self, boxStartRow, boxStartCol, num) -> bool:
        """Input: The starting row and column of a 3 x 3 box, and the targeted number.
        Output: True when the number is present in the box.
        """
        for row in range(boxStartRow, boxStartRow+4):
            for col in range(boxStartCol, boxStartCol+4):
                if self.grid[row, col] == num:
                    return True
        return False

    def findEmptyPlace(self, row, col) -> bool:
        """Input: row and column in the grid.
        Output: If the grid[row, col] is empty, then return true, otherwise false.
        """
        for row in self.grid:
            for column in self.grid:
                if self.grid[row, col] ==0:
                    return True
        return False
        
    def isValidPlace(self, row, col, num) ->bool:
        """Input: Row, a column of the grid, and number to check.
        Output: True, when placing the number at position grid[row, col] is valid.
        """
        # when item not found in col, row and current 3x3 box
        if (not(self.isPresentInRow(row, num)) and not(self.isPresentInCol(col, num)) and not(self.isPresntInBox(row-(row%3), col-(col%3), num))):
            return True

    def solveSudoku(self,Grid) ->bool:
        """Input: The unsolved grid of Sudoku.
        Output: Grid after solve.
        """
        row,col=0,0
        if not self.findEmptyPlace():
            return True
        for n in range(1, 10):
            if self.isValidPlace(row, col, n):
                Grid[row, col] = n
                if self.solveSudoku:
                    return True
                Grid[row, col] = 0
        return False

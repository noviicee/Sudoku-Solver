# About the Project

We are solving the famous number maze problem called [Sudoku](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjN5OjdkqH5AhWNyqACHduhDAUQFnoECAkQAQ&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FSudoku&usg=AOvVaw0uSqpPzYrZ7lA8yesmtFjG).

*Sudoku is a 9 x 9 number grid, and the whole grid are also divided into 3 x 3 boxes There are some rules to solve the Sudoku.*

We have to use digits 1 to 9 for solving this problem.

One digit cannot be repeated in one row, one column or in one 3 x 3 box.

The solution is found using the **backtracking algorithm**. <br>When some cell is filled with a digit, it checks whether it is valid or not. When it is not valid, it checks for other numbers. If all numbers are checked from 1-9, and no valid digit found to place, it backtracks to the previous option.

---

## Input and Output

Input:
<br>This will take a 9 x 9 matrix as Sudoku grid. Some values are placed in the grid. The blank spaces are denoted by 0.

![sudoku-img](images/sudoku-img.jpg)

Output:
<br>The final matrix (Sudoku grid) filled with numbers. If the solution does not exist, it will return false.

![sudoku-img-1](images/sudoku-img-1.png)


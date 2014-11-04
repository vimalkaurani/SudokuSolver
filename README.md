SudokuSolver
============

A Sudoku Solver Algorithm as a part of my Data Structures and Algorithm course. The algorithm has to designed keeping sudoku's of 9x9 to 100x100, and give solution as efficiently as it can.
This is also my first code in Python.
The algorithm works as follows:
1) First it assigns possible candidates for a empty cell in a list corresponding to that position. This is called 'Pencilling-in'. 
Then few elimination rules are implemented, which includes
    i) Single-candidate squares : When a square has just one candidate, that number goes into the square.
    ii) single-square candidates : When a candidate number appears just once in an area (row, column or box), that number goes into the square.
    iii)pairs : When two squares in the same area (row, column or box) have identical two-number candidate lists, you can remove both numbers from other candidate lists in that area.
    

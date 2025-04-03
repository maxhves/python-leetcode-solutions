"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid, but it is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.
"""
from collections import defaultdict
from typing import List


# region Solution

def is_valid_sudoku(board: List[List[str]]) -> bool:
    row_digits = defaultdict(set)
    column_digits = defaultdict(set)
    block_digits = defaultdict(set)

    for row in range(len(board)):
        for column in range(len(board[row])):
            block = (row // 3, column // 3)
            element = board[row][column]

            if element != '.':
                if element in row_digits[row] or element in column_digits[column] or element in block_digits[block]:
                    return False

                row_digits[row].add(element)
                column_digits[column].add(element)
                block_digits[block].add(element)

    return True


# endregion

# region Tests

# True
print(is_valid_sudoku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]))

# False
print(is_valid_sudoku([
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]))

# endregion

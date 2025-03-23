"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
"""
from typing import List


# region Solution

def find_diagonal_order(mat: List[List[int]]) -> List[int]:
    diagonals = []

    rows = len(mat)
    columns = len(mat[0])

    current_row = 0
    current_column = 0

    traversing_up = True

    while len(diagonals) < rows * columns:
        if traversing_up:
            # We should go up and to the right.
            while current_row >= 0 and current_column < columns:
                diagonals.append(mat[current_row][current_column])
                current_column += 1
                current_row -= 1

            if current_column == columns:
                current_column -= 1
                current_row += 2
            else:
                current_row += 1

            traversing_up = False
        else:
            # We should go down and to the left.
            while current_column >= 0 and current_row < rows:
                diagonals.append(mat[current_row][current_column])
                current_column -= 1
                current_row += 1

            if current_row == rows:
                current_row -= 1
                current_column += 2
            else:
                current_column += 1

            traversing_up = True

    return diagonals


# endregion

# region Tests

# [1, 2, 4, 7, 5, 3, 6, 8, 9]
print(find_diagonal_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# [1, 2, 3, 4]
print(find_diagonal_order([[1, 2], [3, 4]]))

# endregion

"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""
from typing import List


# region Solution

# While result array is not the same length as the initial matrix:
# Start traversing right until we reach the end.
# Start traversing down until we reach the end.
# Start traversing left until we reach the end.
# Start traversing up until we reach the end.
# Repeat with the spiral again.
# We need to know about meeting past elements.
# Each time we complete a side the number of rows/columns we can visit should decrease by 1.

def spiral_order(matrix: List[List[int]]) -> List[int]:
    spiral_elements = []

    rows = len(matrix)
    columns = len(matrix[0])

    current_row = 0
    current_column = 0

    right = 0
    down = 0
    left = 0
    up = 0

    direction = "right"

    while len(spiral_elements) < rows * columns:
        if direction == "right":
            while current_column < (columns - right):
                spiral_elements.append(matrix[current_row][current_column])
                current_column += 1

            current_column -= 1
            current_row += 1
            up += 1
            direction = "down"
        elif direction == "down":
            while current_row < (rows - down):
                spiral_elements.append(matrix[current_row][current_column])
                current_row += 1

            current_row -= 1
            current_column -= 1
            right += 1
            direction = "left"
        elif direction == "left":
            while current_column >= (0 + left):
                spiral_elements.append(matrix[current_row][current_column])
                current_column -= 1

            current_column += 1
            current_row -= 1
            down += 1
            direction = "up"
        elif direction == "up":
            while current_row >= (0 + up):
                spiral_elements.append(matrix[current_row][current_column])
                current_row -= 1

            current_column += 1
            current_row = (0 + up)
            left += 1
            direction = "right"

    return spiral_elements


# endregion

# region Tests

# [1, 2, 3, 6, 9, 8, 7, 4, 5
print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
print(spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

# endregion

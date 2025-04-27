"""
Given an m x n binary matrix mat, return the distance of the nearest for each cell.

The distance between two cells sharing a common edge is 1.
"""
import sys
from collections import deque
from typing import List


# region Solution

def update_matrix(mat: List[List[int]]) -> List[List[int]]:
    rows = len(mat)
    columns = len(mat[0])
    cell_queue = deque()

    for mat_row in range(rows):
        for mat_col in range(columns):
            if mat[mat_row][mat_col] == 0:
                cell_queue.append((mat_row, mat_col))
            else:
                mat[mat_row][mat_col] = sys.maxsize

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while len(cell_queue) > 0:
        current_cell = cell_queue.popleft()

        for x, y in directions:
            new_x = current_cell[0] + x
            new_y = current_cell[1] + y

            if 0 <= new_x < rows and 0 <= new_y < columns:
                if mat[new_x][new_y] > mat[current_cell[0]][current_cell[1]] + 1:
                    mat[new_x][new_y] = mat[current_cell[0]][current_cell[1]] + 1
                    cell_queue.append((new_x, new_y))

    return mat


# endregion

# region Tests

# [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(update_matrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))

# [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
print(update_matrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))

# endregion

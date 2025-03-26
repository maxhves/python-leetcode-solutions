"""
Given an integer rowIndex, return the rowIndex th (0-indexed) row of Pascal's triangle.

In Pascal's triangle, each number is the sum of te two numbers directly above it as shown.
"""
from typing import List


# region Solution

def get_row(row_index: int) -> List[int]:
    triangle = [[1]]

    for i in range(row_index):
        prev_level = triangle[i]
        current_level = [1]

        for j in range(i):
            current_level.append(prev_level[j] + prev_level[j + 1])

        current_level.append(1)
        triangle.append(current_level)

    return triangle[row_index]


# endregion

# region Tests

# [1, 3, 3, 1]
print(get_row(3))

# [1]
print(get_row(0))

# [1, 1]
print(get_row(1))

# endregion

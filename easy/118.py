"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown (pretend a diagram is shown).
"""
from typing import List


# region Solution

# Need to know the previous numbers
# Might have to iterate over them at every level :(

def generate(num_rows: int) -> List[List[int]]:
    levels = [[1]]

    for i in range(num_rows - 1):
        prev_level = levels[i]
        current_level = [1]

        for j in range(i):
            current_level.append(prev_level[j] + prev_level[j + 1])

        current_level.append(1)
        levels.append(current_level)

    return levels


# endregion

# region Tests

# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
print(generate(5))

# [[1]]
print(generate(1))

# endregion

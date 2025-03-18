"""
A school is  trying to take an annual photo of all the students. The students are asked to stand in a single file line
in a non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i]
is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each
`heights[i]` is the height of the ith student in line (0-indexed).

Return the number of indices where `heights[i] != expected[i]`.
"""
from typing import List


# region Solution

def height_checker(heights: List[int]) -> int:
    incorrect_placements = 0

    expected = heights.copy()
    expected.sort()

    for i in range(len(heights)):
        if heights[i] != expected[i]:
            incorrect_placements += 1

    return incorrect_placements


# endregion

# region Tests

# 3
print(height_checker([1, 1, 4, 2, 1, 3]))

# 5
print(height_checker([5, 1, 2, 3, 4]))

# 0
print(height_checker([1, 2, 3, 4, 5]))

# endregion

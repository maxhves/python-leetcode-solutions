"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that
they add up to a specific target number. Let these two numbers be numbers[index 1] and numbers[index 2] where 1 <=
index 1 < index 2 <= numbers.length.

Return the indices of the two numbers, index 1 and index 2, added by one as an integer array [index 1, index 2] of
length 2.

Your solution must use only constant extra space.
"""
from typing import List


# region Solution

def two_sum(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1

    while left < right:
        element_sum = numbers[left] + numbers[right]

        if element_sum == target:
            return [left + 1, right + 1]
        elif element_sum > target:
            right -= 1
        else:
            left += 1

    return []


# endregion

# region Tests

# [1, 2]
print(two_sum([2, 7, 11, 15], 9))

# [1, 3]
print(two_sum([2, 3, 4], 6))

# [1, 2]
print(two_sum([-1, 0], -1))

# endregion

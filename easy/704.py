"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function
to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


# region Solution

def search(nums: List[int], target: int) -> int:
    def binary_search(start: int, end: int) -> int:
        if start > end:
            return -1

        middle_element = (start + end) // 2

        if nums[middle_element] == target:
            return middle_element

        if middle_element >= target:
            return binary_search(start, middle_element - 1)
        else:
            return binary_search(middle_element + 1, end)

    return binary_search(0, len(nums) - 1)


# endregion

# region Tests

# 4
print(search([-1, 0, 3, 5, 9, 12], 9))

# -1
print(search([-1, 0, 3, 5, 9, 12], 2))

# endregion

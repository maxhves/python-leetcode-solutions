"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed your function, nums is possibly rotated at an unknown pivot index k
(1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0],
nums[1], ..., nums[k-1] (0-indexed). For example, [0, 1, 2, 3, 4, 5, 6, 7] might be rotated at pivot index
3 and become [4, 5, 6, 7, 0, 1, 2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is
in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


# region Solution

def search(nums: List[int], target: int) -> int:
    def binary_search(start: int, end: int) -> int:
        if start > end:
            return -1

        midpoint = start + ((end - start) // 2)

        if nums[midpoint] == target:
            return midpoint

        left = binary_search(start, midpoint - 1)

        if left == -1:
            return binary_search(midpoint + 1, end)
        else:
            return left

    return binary_search(0, len(nums) - 1)


# endregion

# region Tests

# 4
print(search([4, 5, 6, 7, 0, 1, 2], 0))

# -1
print(search([4, 5, 6, 7, 0, 1, 2], 3))

# -1
print(search([1], 0))

# endregion

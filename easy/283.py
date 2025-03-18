"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
elements.

Note that you must do this in-place without making a copy of the array.
"""
from typing import List


# region Solution

def move_zeroes(nums: List[int]) -> List[int]:
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0 and nums[left] == 0:
            nums[left] = nums[right]
            nums[right] = 0

        if nums[left] != 0:
            left += 1

    return nums


# endregion

# region Tests

# [2, 1]
print(move_zeroes([2, 1]))

# [1, 0]
print(move_zeroes([1, 0]))

# [1, 3, 12, 0, 0]
print(move_zeroes([0, 1, 0, 3, 12]))

# [0]
print(move_zeroes([0]))

# endregion

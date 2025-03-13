"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
non-decreasing order.
"""
from typing import List


# region Solution

def sorted_squares(nums: List[int]) -> List[int]:
    for index, num in enumerate(nums):
        nums[index] = num * num

    nums.sort()
    return nums


# endregion

# region Tests

# [0, 1, 9, 16, 100]
print(sorted_squares([-4, -1, 0, 3, 10]))

# [4, 9, 9, 49, 121]
print(sorted_squares([-7, -3, 2, 3, 11]))

# endregion

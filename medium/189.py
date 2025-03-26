"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""
from typing import List


# region Solution

def rotate(nums: List[int], k: int) -> List[int]:
    nums_length = len(nums)
    rotated = [0] * nums_length
    real_rotation = k % nums_length

    for i in range(nums_length):
        new_element_position = i + real_rotation

        if new_element_position > (nums_length - 1):
            new_element_position = new_element_position - nums_length

        rotated[new_element_position] = nums[i]

    for i in range(len(rotated)):
        nums[i] = rotated[i]

    return nums


# endregion

# region Tests

# [5, 6, 7, 1, 2, 3, 4]
print(rotate([1, 2, 3, 4, 5, 6, 7], 3))

# [3, 99, -1, -100]
print(rotate([-1, -100, 3, 99], 2))

# endregion

"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the
range [1, n] that do not appear in nums.
"""
from typing import List


# region Solution

def find_disappeared_numbers(nums: List[int]) -> List[int]:
    nums_set = set(nums)
    missing = []

    for i in range(len(nums)):
        if i + 1 not in nums_set:
            missing.append(i + 1)

    return missing


# endregion

# region Tests

# [5, 6]
print(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))

# [2]
print(find_disappeared_numbers([1, 1]))

# endregion

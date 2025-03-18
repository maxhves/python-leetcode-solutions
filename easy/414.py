"""
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not
exist, return the maximum number.
"""
from typing import List


# region Solution

def third_max(nums: List[int]) -> int:
    nums = sorted(set(nums), reverse=True)

    if len(nums) < 3:
        return nums[0]
    else:
        return nums[2]


# endregion

# region Tests

# 2
print(third_max([1, 2, 2]))

# 1
print(third_max([3, 2, 1]))

# 2
print(third_max([1, 2]))

# 1
print(third_max([2, 2, 3, 1]))

# endregion

"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and only use constant extra space.
"""
from typing import List


# region Solution

def single_number(nums: List[int]) -> int:
    nums_set = set()

    for num in nums:
        if num not in nums_set:
            nums_set.add(num)
        else:
            nums_set.remove(num)

    return nums_set.pop()


# endregion

# region Tests

# 1
print(single_number([2, 2, 1]))

# 4
print(single_number([4, 1, 2, 1, 2]))

# 1
print(single_number([1]))

# endregion

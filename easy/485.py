"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""
from typing import List


# region Solution

def find_max_consecutive_ones(nums: List[int]) -> int:
    max_consecutive = 0
    current_consecutive = 0

    for num in nums:
        if num == 1:
            current_consecutive += 1
            max_consecutive = max(max_consecutive, current_consecutive)
        else:
            current_consecutive = 0

    return max_consecutive


# endregion

# region Tests

# 3
print(find_max_consecutive_ones([1, 1, 0, 1, 1, 1]))

# 2
print(find_max_consecutive_ones([1, 0, 1, 1, 0, 1]))

# endregion

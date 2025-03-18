"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""
from typing import List


# region Solution

def sort_array_by_parity(nums: List[int]) -> List[int]:
    left = 0

    for right in range(len(nums)):
        if nums[left] % 2 != 0 and nums[right] % 2 == 0:
            left_original = nums[left]

            nums[left] = nums[right]
            nums[right] = left_original

        if nums[left] % 2 == 0:
            left += 1

    return nums


# endregion

# region Tests

# [2, 4, 3, 1]
print(sort_array_by_parity([3, 1, 2, 4]))

# [0]
print(sort_array_by_parity([0]))

# endregion

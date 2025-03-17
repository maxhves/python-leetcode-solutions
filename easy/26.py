"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element
appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements
in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
- Change the array nums such that the first k elements of nums contain the unique elements in the order they were
  present in nums initially. The remaining elements of nums are not important as well as the size of nums.
- Return k.
"""
from typing import List


# region Solution

def remove_duplicates(nums: List[int]) -> int:
    left = 1

    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1

    return left


# endregion

# region Tests

# 2, nums = [1, 2, _]
print(remove_duplicates([1, 1, 2]))

# 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

# endregion

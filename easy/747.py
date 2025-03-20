"""
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it
is, return the index of the largest element, or return -1 otherwise.
"""
from typing import List


# region Solution

def dominant_index(nums: List[int]) -> int:
    prev_max_element_index = 0
    max_element_index = 0

    for i in range(len(nums)):
        if nums[i] > nums[max_element_index]:
            prev_max_element_index = max_element_index
            max_element_index = i
        elif nums[i] > nums[prev_max_element_index]:
            prev_max_element_index = i

        if prev_max_element_index == max_element_index:
            prev_max_element_index = i

    return max_element_index if (nums[prev_max_element_index] * 2) <= nums[max_element_index] else -1


# endregion

# region Tests

# 0
print(dominant_index([1, 0]))

# 1
print(dominant_index([3, 6, 1, 0]))

# -1
print(dominant_index([1, 2, 3, 4]))

# endregion

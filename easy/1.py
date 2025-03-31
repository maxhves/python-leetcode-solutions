"""
Given an aray of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List


# region Solution

def two_sum(nums: List[int], target: int) -> List[int]:
    occurrences = {}

    for i in range(len(nums)):
        current_element = nums[i]

        if current_element not in occurrences:
            occurrences[current_element] = i

        if (target - current_element) in occurrences:
            if occurrences[target - current_element] != i:
                return [i, occurrences[target - current_element]]

    return []


# endregion

# region Tests

# [0, 1]
print(two_sum([2, 7, 11, 15], 9))

# [1, 2]
print(two_sum([3, 2, 4], 6))

# [0, 1]
print(two_sum([3, 3], 6))

# endregion

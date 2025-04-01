"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such
that nums[i] == nums[j] and abs(i - j) <= k.
"""
from typing import List


# region Solution

def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    occurrences = {}

    for i in range(len(nums)):
        element = nums[i]

        if element in occurrences:
            prev_index = occurrences[element]

            if abs(prev_index - i) <= k:
                return True

        occurrences[element] = i

    return False


# endregion

# region Tests

# True
print(contains_nearby_duplicate([1, 2, 3, 1], 3))

# True
print(contains_nearby_duplicate([1, 0, 1, 1], 1))

# False
print(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))

# endregion

"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
element is distinct.
"""
from typing import List


# region Solution

def contains_duplicates(nums: List[int]) -> bool:
    hashset = set()

    for num in nums:
        if num in hashset:
            return True
        else:
            hashset.add(num)

    return False


# endregion

# region Tests

# True
print(contains_duplicates([1, 2, 3, 1]))

# False
print(contains_duplicates([1, 2, 3, 4]))

# True
print(contains_duplicates([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

# endregion

"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be
unique, and you may return the result in any order.
"""
from typing import List


# region Solution

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1_set = set()
    results = set()

    for num1 in nums1:
        nums1_set.add(num1)

    for num2 in nums2:
        if num2 in nums1_set:
            results.add(num2)

    return list(results)


# endregion

# region Tests

# [2]
print(intersection([1, 2, 2, 1], [2, 2]))

# [9, 4]
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))

# endregion

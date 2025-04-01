"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear
as many times as it shows in both arrays, and you may return the result in any order.
"""
from typing import List


# region Solution

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1_occurrences = {}
    result = []

    for i in range(len(nums1)):
        element = nums1[i]

        if element in nums1_occurrences:
            nums1_occurrences[element] += 1
        else:
            nums1_occurrences[element] = 1

    for i in range(len(nums2)):
        element = nums2[i]

        if element in nums1_occurrences and nums1_occurrences[element] > 0:
            result.append(element)
            nums1_occurrences[element] -= 1

    return result


# endregion

# region Tests

# [2, 2]
print(intersect([1, 2, 2, 1], [2, 2]))

# [4, 9]
print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))

# endregion

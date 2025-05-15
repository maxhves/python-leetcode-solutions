"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains
multiple peaks, return the index to any of them peaks.

You may imagine that nums[-1] = nums[n] = -infinity. In other works, an element is always considered to
be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
"""
from typing import List


# region Solution

def find_peak_element(nums: List[int]) -> int:
    def binary_search(start: int, end: int) -> int:
        if start > end:
            return -1

        midpoint = start + ((end - start) // 2)

        if midpoint > 0 and nums[midpoint] < nums[midpoint - 1]:
            return binary_search(start, midpoint - 1)
        elif midpoint < len(nums) - 1 and nums[midpoint] < nums[midpoint + 1]:
            return binary_search(midpoint + 1, end)
        else:
            return midpoint

    return binary_search(0, len(nums) - 1)


# endregion

# region Tests

# 2
print(find_peak_element([1, 2, 3, 1]))

# 5
print(find_peak_element([1, 2, 1, 3, 5, 6, 4]))

# endregion

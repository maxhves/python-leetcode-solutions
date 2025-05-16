"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of
a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


# region Solution

# We need to utilize two binary arrays to find the start and end.

def search_range(nums: List[int], target: int) -> List[int]:
    start_result = -1
    end_result = -1

    start = 0
    end = len(nums) - 1

    while start <= end:
        midpoint = start + ((end - start) // 2)

        if nums[midpoint] < target:
            start = midpoint + 1
        elif nums[midpoint] > target:
            end = midpoint - 1
        else:
            start_result = midpoint
            end = midpoint - 1

    start = 0
    end = len(nums) - 1

    while start <= end:
        midpoint = start + ((end - start) // 2)

        if nums[midpoint] < target:
            start = midpoint + 1
        elif nums[midpoint] > target:
            end = midpoint - 1
        else:
            end_result = midpoint
            start = midpoint + 1

    return [start_result, end_result]


# endregion

# region Tests

# [3, 4]
print(search_range([5, 7, 7, 8, 8, 10], 8))

# [-1, -1]
print(search_range([5, 7, 7, 8, 8, 10], 6))

# [-1, -1]
print(search_range([], 0))

# endregion

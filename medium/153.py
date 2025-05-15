"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the
array n = [0, 1, 2, 4, 5, 6, 7] might become:
- [4, 5, 6, 7, 0, 1, 2] if it was rotated 4 times.
- [0, 1, 2, 4, 5, 6, 7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1],
a[2], ..., a[n-2]].

Given the sorted array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""
from typing import List


# region Solution

def find_min(nums: List[int]) -> int:
    def binary_search(start: int, end: int, current_min: int) -> int:
        if start > end:
            return current_min

        midpoint = start + ((end - start) // 2)

        new_min = min(current_min, nums[midpoint])

        if nums[midpoint] > nums[end]:
            return binary_search(midpoint + 1, end, new_min)
        else:
            return binary_search(start, midpoint - 1, new_min)

    return binary_search(0, len(nums) - 1, nums[0])


# endregion

# region Tests

# 1
print(find_min([3, 4, 5, 1, 2]))

# 0
print(find_min([4, 5, 6, 7, 0, 1, 2]))

# 11
print(find_min([11, 13, 15, 17]))

# endregion

"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum
of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This
also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""
from typing import List


# region Solution

def pivot_index(nums: List[int]) -> int:
    prefix_sum = []

    for i in range(len(nums)):
        if i == 0:
            prefix_sum.append(nums[0])
        else:
            prefix_sum.append(nums[i] + prefix_sum[i - 1])

    for i in range(len(nums)):
        right_sum = prefix_sum[len(nums) - 1] - prefix_sum[i]
        left_sum = prefix_sum[i - 1] if i != 0 else 0

        if right_sum == left_sum:
            return i

    return -1


# endregion

# region Tests

# 3
print(pivot_index([1, 7, 3, 6, 5, 6]))

# -1
print(pivot_index([1, 2, 3]))

# 0
print(pivot_index([2, 1, -1]))

# endregion

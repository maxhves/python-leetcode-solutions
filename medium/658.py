"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
The result should also be sorted in ascending order.

An integer 'a' is closer to x than an integer 'b' if:
- |a - x| < |b - x|, or
- |a - x| == |b - x| and a < b
"""
from typing import List


# region Solution

def find_closest_elements(arr: List[int], k: int, x: int) -> List[int]:
    start = 0
    end = len(arr) - k

    while start < end:
        midpoint = start + ((end - start) // 2)

        if x - arr[midpoint] > arr[midpoint + k] - x:
            start = midpoint + 1
        else:
            end = midpoint

    return arr[start:start + k]


# endregion

# region Tests

# [1, 2, 3, 4]
print(find_closest_elements([1, 2, 3, 4, 5], 4, 3))

# [1, 1, 2, 3]
print(find_closest_elements([1, 1, 2, 3, 4, 5], 4, -1))

# endregion

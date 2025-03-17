"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:
- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
  - arr[0] < arr[1] < ... < arr[i - 1] <arr[i]
  - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""
from typing import List


# region Solution

def valid_mountain_array(arr: List[int]) -> bool:
    i = 1

    while i < len(arr) and arr[i] > arr[i - 1]:
        i += 1

    if i == 1 or i == len(arr):
        return False

    while i < len(arr) and arr[i] < arr[i - 1]:
        i += 1

    return i == len(arr)


# endregion

# region Tests

# false
print(valid_mountain_array([0, 1, 2, 1, 2]))

# false
print(valid_mountain_array([2, 1]))

# false
print(valid_mountain_array([3, 5, 5]))

# true
print(valid_mountain_array([0, 3, 2, 1]))

# false
print(valid_mountain_array([2, 0, 2]))

# endregion

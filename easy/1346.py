"""
Given an array arr of integers, check if there exists two indices i and j such that:
- i != j
- 0 <= i, j < arr.length
- arr[i] == 2 * arr[j]
"""
from typing import List


# region Solution

# Two pointers
# 1. Set left to 0.
# 2. While left is smaller than arr length.
# 3. Set right to left + 1.
# 4. Iterate from right to end, check if a number exists that is half of or double arr[left].
# 5. Return True immediately if we find a case.

def check_if_exists(arr: List[int]) -> bool:
    left = 0

    while left < len(arr):
        for right in range(left + 1, len(arr)):
            if arr[left] == (arr[right] * 2) or arr[left] == (arr[right] / 2):
                return True
        left += 1

    return False


# endregion

# region Tests

# ture
print(check_if_exists([10, 2, 5, 3]))

# false
print(check_if_exists([3, 1, 7, 11]))

# endregion

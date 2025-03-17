"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right,
and replace the last element with -1.

After doing so, return the array.
"""
from typing import List


# region Solution

def replace_elements(arr: List[int]) -> List[int]:
    max_element = arr[len(arr) - 1]

    for i in range(len(arr) - 2, -1, -1):
        current_element = arr[i]
        arr[i] = max_element
        max_element = max(max_element, current_element)

    arr[len(arr) - 1] = -1
    return arr


# endregion

# region Tests

# [18, 6, 6, 6, 1, -1]
print(replace_elements([17, 18, 5, 4, 6, 1]))

# [-1]
print(replace_elements([400]))

# endregion

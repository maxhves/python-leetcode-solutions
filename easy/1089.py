"""
Given a fixed-length array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input
array in place and do not return anything.
"""
from typing import List


# region Solution

def duplicate_zeros(arr: List[int]) -> List[int]:
    possible_dupes = 0
    length_ = len(arr) - 1

    for left in range(length_ + 1):

        if left > length_ - possible_dupes:
            break

        if arr[left] == 0:
            if left == length_ - possible_dupes:
                arr[length_] = 0
                length_ -= 1
                break
            possible_dupes += 1

    last = length_ - possible_dupes

    for i in range(last, -1, -1):
        if arr[i] == 0:
            arr[i + possible_dupes] = 0
            possible_dupes -= 1
            arr[i + possible_dupes] = 0
        else:
            arr[i + possible_dupes] = arr[i]

    return arr


# endregion

# region Tests

# [0,0,0,0,0,0,0]
print(duplicate_zeros([0, 0, 0, 0, 0, 0]))

# [1, 0, 0, 2, 3, 0, 0, 4]
print(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]))

# [1, 2, 3]
print(duplicate_zeros([1, 2, 3]))

# endregion

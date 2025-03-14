"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing
the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead should be stored inside the array nums1. To
accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and
the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""
from typing import List


# region Solution

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    nums1_length = len(nums1)
    last_num1_index = m

    if n == 0:
        return nums1

    for num2 in nums2:
        for i in range(0, nums1_length):
            num1 = nums1[i]

            if num1 > num2:
                for j in range(last_num1_index, i, -1):
                    nums1[j] = nums1[j - 1]

                nums1[i] = num2
                last_num1_index += 1
                break
            elif i == last_num1_index:
                nums1[i] = num2
                last_num1_index += 1
                break

    return nums1


# endregion

# region Tests

# [1, 2, 2, 3, 5, 6]
print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))

# [1]
print(merge([1], 1, [], 0))

# [1]
print(merge([0], 0, [1], 1))

# endregion

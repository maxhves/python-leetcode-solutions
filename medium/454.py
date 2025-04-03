"""
Given four integer arrays nums1, nums2, nums3 and nums4 all length n, return the number of tuples (i, j, k, l) such
that:
- 0 <= i, j, k, l < n
- nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
"""
from collections import defaultdict
from typing import List


# region Solution

def four_sum_count(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    sums = defaultdict(int)
    zero_sums = 0

    for i in range(len(nums1)):
        num1 = nums1[i]

        for j in range(len(nums2)):
            num2 = nums2[j]

            sums[num1 + num2] += 1

    for k in range(len(nums3)):
        num3 = nums3[k]

        for l in range(len(nums4)):
            num4 = nums4[l]

            remainder_needed = 0 - (num3 + num4)

            if remainder_needed in sums:
                zero_sums += sums[remainder_needed]

    return zero_sums


# endregion

# region Tests

# 6
print(four_sum_count([-1, -1], [-1, 1], [-1, 1], [1, -1]))

# 2
print(four_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2]))

# 1
print(four_sum_count([0], [0], [0], [0]))

# endregion

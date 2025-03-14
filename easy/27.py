"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not
equal to val.

Consider the number of elements in nums which are not equal to val to be k, to get accepted you need to do the following
things:
- Change the array nums such that thr first k elements of nums contain the elements which ate not equal to val. The
  remaining elements of nums ar enot important as wel as the size of nums.
- Return k.
"""
from typing import List


# region Solution

def remove_element(nums: List[int], val: int) -> int:
    length = len(nums)

    i = 0

    while i < length:
        num = nums[i]

        # We need to remove this value
        if num == val:

            for j in range(i + 1, length):
                nums[j - 1] = nums[j]

            length -= 1

        if nums[i] != val:
            i += 1

    return length


# endregion

# region Tests

# 2, nums = [2, 2, _, _ ]
print(remove_element([3, 2, 2, 3], 3))

# 5, nums = [0, 1, 4, 0, 3, _, _, _]
print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))

# endregion

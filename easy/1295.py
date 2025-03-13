"""
Given an array nums of integers, return how many of them contain an even number of digits.
"""
from typing import List


# region Solution

def find_numbers(nums: List[int]) -> int:
    even_digit_counts = 0

    for num in nums:
        num_str = str(num)

        if len(num_str) & 1 == 0:
            even_digit_counts += 1

    return even_digit_counts


# endregion

# region Tests

# 2
print(find_numbers([12, 345, 2, 6, 7896]))

# 1
print(find_numbers([555, 901, 482, 1771]))

# endregion

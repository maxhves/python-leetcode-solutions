"""
You are given a large integer represented as an integer array digits, where each digit[i] is the ith digit of the
integer. The digits are ordered from most significant in the left-to-right order. The large integer does not contain
any leading 0's.
"""
from typing import List


# region Solution

def plus_one(digits: List[int]) -> List[int]:
    length = len(digits)
    current_index = length - 1

    if digits[current_index] == 9:
        # While the current element is a 9.
        while digits[current_index] == 9:
            digits[current_index] = 0
            current_index -= 1

        # We are at the index which is not a 9.
        if current_index == -1:
            digits[0] = 1
            digits.append(0)
        else:
            digits[current_index] += 1

    else:
        digits[current_index] += 1

    return digits


# endregion

# region Tests

# [1, 2, 4]
print(plus_one([1, 2, 3]))

# [4, 3, 2, 2]
# print(plus_one([4, 3, 2, 1]))

# [1, 0]
# print(plus_one([9]))

# endregion

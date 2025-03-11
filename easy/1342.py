"""
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
"""


# region Solution

def number_of_steps_modulo(num: int) -> int:
    steps = 0

    while num > 0:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1

        steps += 1

    return steps


def number_of_steps_bitwise(num: int) -> int:
    steps = 0

    while num > 0:
        if num & 1 == 0:
            num = num >> 1
        else:
            num -= 1

        steps += 1

    return steps


# endregion

# region Tests

# 6
print(number_of_steps_modulo(14))
print(number_of_steps_bitwise(14))

# 4
print(number_of_steps_modulo(8))
print(number_of_steps_bitwise(8))

# 12
print(number_of_steps_modulo(123))
print(number_of_steps_bitwise(123))

# endregion

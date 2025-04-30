"""
given a non-negative integer x, return the square root of x rounded down to the nearest integer. The
returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
- For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""


# region Solution

# Generate a list of numbers from 0 to x.
# Binary search for a number that when multiplied by 2 is equal to x.

def my_sqrt(x: int) -> int:
    start = 0
    end = x
    last_result = 0

    while start <= end:
        middle = start + ((end - start) // 2)
        square_middle = middle * middle

        if square_middle > x:
            end = middle - 1
        elif square_middle < x:
            start = middle + 1
            last_result = middle
        else:
            return middle

    return last_result


# endregion

# region Tests

# 2
print(my_sqrt(4))

# 2
print(my_sqrt(8))

# endregion

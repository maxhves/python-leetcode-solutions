"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with
itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
"""


# region Solution

def num_squares(n: int) -> int:
    results = [n] * (n + 1)
    results[0] = 0

    for target in range(1, n + 1):
        for s in range(1, target + 1):
            square = s * s

            if target - square < 0:
                break

            results[target] = min(results[target], 1 + results[target - square])

    return results[n]


# endregion

# region Tests

# 3
print(num_squares(12))

# 2
print(num_squares(13))

# endregion

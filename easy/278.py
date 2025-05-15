"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest
version of your product fails the quality check. Since each version is developed based on the previous
version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all
the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function
to find the first bad version. You should minimize the number of calls to the API.
"""


# region Solution

def is_bad_version(version: int) -> int:
    return version == 4


def first_bad_version(n: int) -> int:
    def binary_search(start: int, end: int) -> int:
        if start > end:
            return start

        midpoint = start + ((end - start) // 2)

        if is_bad_version(midpoint):
            return binary_search(start, midpoint - 1)
        else:
            return binary_search(midpoint + 1, end)

    return binary_search(0, n)


# endregion

# region Tests

# 4
print(first_bad_version(5))

# endregion

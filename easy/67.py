"""
Given two binary strings a and b, return their sum as a binary string.
"""


# region Solution

def add_binary(a: str, b: str) -> str:
    return format(int(a, 2) + int(b, 2), 'b')


# endregion

# region Tests

# 100
print(add_binary("11", "1"))

# 10101
print(add_binary("1010", "1011"))

# endregion

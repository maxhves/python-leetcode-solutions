"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.
"""


# region Solution

def str_str(haystack: str, needle: str) -> int:
    current_str = haystack

    while len(current_str) > 0:
        if not current_str.startswith(needle):
            current_str = current_str[1:]
        else:
            return len(haystack) - len(current_str)

    return -1


# endregion

# region Tests

# 2
print(str_str("abc", "c"))

# 0
print(str_str("sadbutsad", "sad"))

# -1
print(str_str("leetcode", "leeto"))

# endregion

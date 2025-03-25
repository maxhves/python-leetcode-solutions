"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.
"""


# region Solution

# Let's use two pointers to iterate over haystack.
# Left will track the beginning of the string.
# Right will track characters matching in needle.
# If right pointer exceeds past the length of needle, we found a match, return left
# Otherwise just return -1.

# We can't assume that when we have checked a whole string that left will begin from end of that string check
# We have to check every single position of the string.

def str_str(haystack: str, needle: str) -> int:
    return 0


# endregion

# region Tests

# 2
print(str_str("abc", "c"))

# 0
print(str_str("sadbutsad", "sad"))

# -1
print(str_str("leetcode", "leeto"))

# endregion

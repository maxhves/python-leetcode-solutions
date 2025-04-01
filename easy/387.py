"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist
return -1.
"""


# region Solution

def first_unique_char(s: str) -> int:
    occurrences = {}

    for i in range(len(s)):
        char = s[i]

        if char in occurrences:
            occurrences[char] = occurrences[char] + 1
        else:
            occurrences[char] = 1

    for i in range(len(s)):
        if occurrences[s[i]] == 1:
            return i

    return -1


# endregion

# region Tests

# 0
print(first_unique_char("leetcode"))

# 2
print(first_unique_char("loveleetcode"))

# -1
print(first_unique_char("aabb"))

# endregion

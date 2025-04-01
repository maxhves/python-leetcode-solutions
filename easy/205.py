"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No
two characters may map to the same character, but a character may map to itself.
"""


# region Solution

def is_isomorphic(s: str, t: str) -> bool:
    s_occurrences = {}
    t_occurrences = {}

    for i in range(len(s)):
        if s[i] not in s_occurrences:
            s_occurrences[s[i]] = i

        if t[i] not in t_occurrences:
            t_occurrences[t[i]] = i

        if s_occurrences[s[i]] != t_occurrences[t[i]]:
            return False

    return True


# endregion

# region Tests

# True
print(is_isomorphic("egg", "add"))

# False
print(is_isomorphic("foo", "bar"))

# True
print(is_isomorphic("paper", "title"))

# endregion

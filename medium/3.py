"""
Given a string s, find the length of the longest substring without duplicate characters.
"""


# region Solution

def length_of_longest_substring(s: str) -> int:
    max_substring_length = 0
    char_occurrences = {}

    left = 0
    for right in range(len(s)):

        if s[right] not in char_occurrences or char_occurrences[s[right]] < left:
            char_occurrences[s[right]] = right
            max_substring_length = max(max_substring_length, right - left + 1)
        else:
            left = char_occurrences[s[right]] + 1
            char_occurrences[s[right]] = right

    return max_substring_length


# endregion

# region Tests

# 6
print(length_of_longest_substring("ggububgvfk"))

# 3
print(length_of_longest_substring("abcabcbb"))

# 1
print(length_of_longest_substring("bbbbb"))

# 3
print(length_of_longest_substring("pwwkew"))

# endregion

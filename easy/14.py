"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
from typing import List


# region Solution

def longest_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ""

    prefix = strs[0]

    for i in range(len(strs)):
        current_str = strs[i]

        while not current_str.startswith(prefix):
            prefix = prefix[:-1]

            if not prefix:
                return ""

    return prefix


# endregion

# region Tests

# fl
print(longest_common_prefix(["flower", "flow", "flight"]))

# ""
print(longest_common_prefix(["dog", "racecar", "car"]))

# endregion

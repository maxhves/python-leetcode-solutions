"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List


# region Solution

def reverse_string(s: List[str]) -> List[str]:
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s


# endregion

# region Tests

# ["o", "l", "l", "e", "h"]
print(reverse_string(["h", "e", "l", "l", "o"]))

# ["h", "a", "n", "n", "a", "h"]
print(reverse_string(["h", "a", "n", "n", "a", "h"]))

# endregion

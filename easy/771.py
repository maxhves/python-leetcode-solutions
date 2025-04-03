"""
You're given strings jewels representing the types of stones that jewels, and stones representing the stones you have.
Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case-sensitive, so "a" is considered a different type of stone from "A".
"""


# region Solution

def num_jewels_in_stones(jewels: str, stones: str) -> int:
    jewel_count = 0
    jewels_set = set(jewels)

    for stone in stones:
        if stone in jewels_set:
            jewel_count += 1

    return jewel_count


# endregion

# region Tests

# 3
print(num_jewels_in_stones("aA", "aAAbbbb"))

# 0
print(num_jewels_in_stones("z", "ZZ"))

# endregion

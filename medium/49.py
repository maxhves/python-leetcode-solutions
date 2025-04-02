"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""
from typing import List


# region Solution

# Create a groups hash map.
# For each string in the array:
# - Order the string.
# - Use this as a key.
# - Check if the key exists:
#   - If exists, add original string to a list stored at the key.
#   - Else add a new list at the key, containing the original string.
# Return the group hash map as a list.

def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = {}

    for i in range(len(strs)):
        element_ordered = ''.join(sorted(strs[i]))

        if element_ordered in groups:
            groups[element_ordered].append(strs[i])
        else:
            new_group = [strs[i]]
            groups[element_ordered] = new_group

    return list(groups.values())


# endregion

# region Tests

# [["bat"],["nat","tan"],["ate","eat","tea"]]
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# [[""]]
print(group_anagrams([""]))

# [["a"]]
print(group_anagrams(["a"]))

# endregion

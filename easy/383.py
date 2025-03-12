"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters
from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""


# region Solution

def can_construct(ransom_note: str, magazine: str) -> bool:
    magazine_occurrences = {}

    for char in magazine:
        if char in magazine_occurrences:
            magazine_occurrences[char] = magazine_occurrences[char] + 1
        else:
            magazine_occurrences[char] = 1

    for char in ransom_note:
        if char in magazine_occurrences:
            if magazine_occurrences[char] == 0:
                return False
            else:
                magazine_occurrences[char] = magazine_occurrences[char] - 1
        else:
            return False

    return True


# endregion

# region Tests

#  false
print(can_construct("a", "b"))

# false
print(can_construct("aa", "ab"))

# true
print(can_construct("aa", "aab"))

# endregion

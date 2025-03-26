"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of none-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order, concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should
only have a single space separating the words. Do not include any extra spaces.
"""


# region Solution

def reverse_words(s: str) -> str:
    words = s.split()
    reversed_words = []

    for i in range(len(words) - 1, -1, -1):
        reversed_words.append(words[i])

        if i != 0:
            reversed_words.append(" ")

    return "".join(reversed_words)


# endregion

# region Tests

# blue is sky the
print(reverse_words("the sky is blue"))

# world hello
print(reverse_words("  hello world  "))

# example good a
print(reverse_words("a good   example"))

# endregion

"""
Given a string s, reverse the order of the characters in each word withing a sentence while still preserving whitespace
and initial word order.
"""


# region Solution

def reverse_words(s: str) -> str:
    words = s.split()
    reversed_words = []

    for word in words:
        current_word = ""
        for i in range(len(word) - 1, -1, -1):
            current_word += word[i]

        reversed_words.append(current_word)

    return " ".join(reversed_words)


# endregion

# region Tests

# s'teL ekat edoCteeL tsetnoc
print(reverse_words("Let's take LeetCode contest"))

# rM gniD
print(reverse_words("Mr Ding"))

# endregion

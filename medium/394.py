"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being
repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaced, square brackets are
well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that
digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
"""


# region Solution

def decode_string(s: str) -> str:
    stack = []

    for i in range(len(s)):
        char = s[i]

        if char != "]":
            stack.append(char)
        else:
            substring = ""

            while stack[-1] != "[":
                substring = stack.pop() + substring

            stack.pop()

            to_repeat = ""
            while stack and stack[-1].isdigit():
                to_repeat = stack.pop() + to_repeat

            stack.append(int(to_repeat) * substring)

    return "".join(stack)


# endregion

# region Tests

# aaabcbc
print(decode_string("3[a]2[bc]"))

# accaccacc
print(decode_string("3[a2[c]]"))

# abcabccdcdcdef
print(decode_string("2[abc]3[cd]ef"))

# endregion

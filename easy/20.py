"""
Given a string s containing just the characters '(', ')', '{', '}', '[', ']', determine if the input string
is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
"""


# region Solution

def is_valid(s: str) -> bool:
    bracket_stack = []
    open_bracket_types = {"(", "[", "{"}

    def bracket_matches(current: str, top: str) -> bool:
        if current == ")":
            return top == "("
        elif current == "]":
            return top == "["
        else:
            return top == "{"

    for bracket in s:
        if bracket in open_bracket_types:
            bracket_stack.append(bracket)
        else:
            if len(bracket_stack) == 0:
                return False

            top_bracket = bracket_stack.pop()

            if not bracket_matches(bracket, top_bracket):
                return False

    return len(bracket_stack) == 0


# endregion

# region Tests

# True
print(is_valid("()"))

# True
print(is_valid("()[]{}"))

# False
print(is_valid("(]"))

# True
print(is_valid("([])"))

# endregion

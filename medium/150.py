"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish
Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notion.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""
from math import trunc
from typing import List


# region Solution

def eval_rpn(tokens: List[str]) -> int:
    operations = {"+", "-", "*", "/"}
    operands = []

    for token in tokens:
        if token in operations:
            second = operands.pop()
            first = operands.pop()

            if token == "+":
                operands.append(first + second)
            elif token == "-":
                operands.append(first - second)
            elif token == "*":
                operands.append(first * second)
            else:
                operands.append(trunc(first / second))
        else:
            operands.append(int(token))

    return operands.pop()


# endregion

# region Tests

# 9
print(eval_rpn(["2", "1", "+", "3", "*"]))

# 6
print(eval_rpn(["4", "13", "5", "/", "+"]))

# 22
print(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

# endregion

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
"""


# region Solution

class MinStack:

    def __init__(self):
        self.current_min = 0
        self.stack = []
        self.size = 0

    def push(self, val: int) -> None:
        if self.size == 0:
            self.current_min = val
        else:
            self.current_min = min(self.current_min, val)

        self.stack.append((val, self.current_min))
        self.size += 1

    def pop(self) -> None:
        if self.size == 0:
            return

        self.stack.pop()
        self.size -= 1

        if self.size > 0:
            self.current_min = self.stack[self.size - 1][1]

    def top(self) -> int:
        return self.stack[self.size - 1][0]

    def getMin(self) -> int:
        return self.current_min


# endregion

# region Tests

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
# -3
print(minStack.getMin())
minStack.pop()
# 0
print(minStack.top())
# -2
print(minStack.getMin())

# endregion

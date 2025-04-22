"""
Implement a list-in-first-out (LIFO) stack using only two queues. The implemented stack should support all
the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:
- void push(int x) Pushes element x to the top of the stack.
- int pop() Removes the element on the top of the stack and returns it.
- int top() Returns the element on the top of the stack.
- boolean empty() Returns true if the stack is empty, false otherwise.
"""
from collections import deque


# region Solution

class MyStack:

    def __init__(self):
        self.queue = deque()
        self.list = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[len(self.queue) - 1]

    def empty(self) -> bool:
        return len(self.queue) == 0


# endregion

# region Tests

myStack = MyStack()
myStack.push(1)
myStack.push(2)
myStack.top()
myStack.empty()

# endregion

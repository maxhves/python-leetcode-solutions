"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all
the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.

You must use only standard operations of a stack, which means only 'push to top', 'peek/pop from top', 'size' and
'is empty' operations are valid.

Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or
deque (double-ended queue) as long as you use only a stack's standard operations.
"""


# region Solution

# Read stack
# Write stack

class MyQueue:

    def __init__(self):
        self.read_stack = []
        self.write_stack = []

    def push(self, x: int) -> None:
        self.write_stack.append(x)

    def pop(self) -> int:
        if len(self.read_stack) == 0:
            while len(self.write_stack) > 0:
                self.read_stack.append(self.write_stack.pop())

        return self.read_stack.pop()

    def peek(self) -> int:
        if len(self.read_stack) == 0:
            while len(self.write_stack) > 0:
                self.read_stack.append(self.write_stack.pop())

        return self.read_stack[len(self.read_stack) - 1]

    def empty(self) -> bool:
        return len(self.read_stack) == 0 and len(self.write_stack) == 0


# endregion

# region Tests

myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
myQueue.peek()
myQueue.pop()
myQueue.empty()

# endregion

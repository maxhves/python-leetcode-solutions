"""
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations
are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position
to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make sue of the spaces in front of the queue. In a normal queue
once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using
the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:
- MyCircularQueue(k) Initializes the object with the size of the queue to be k.
- int Front() Gets the front item from the queue. If the queue is empty, return -1.
- int Rear() Gets the last item from the queue. If the queue is empty, return -1.
- boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
- boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
- boolean isEmpty() Checks whether the circular queue is empty or not.
- boolean isFully() Checks whether the circular queue is full or not.
"""


# region Solution

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.circular_queue = [0] * k
        self.head = -1
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.head = 0

        self.tail = (self.tail + 1) % self.size
        self.circular_queue[self.tail] = value

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True

        self.head = (self.head + 1) % self.size

        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.circular_queue[self.head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.circular_queue[self.tail]

    def isEmpty(self) -> bool:
        return self.head == -1

    def isFull(self) -> bool:
        return ((self.tail + 1) % self.size) == self.head


# endregion


# region Tests

myCircularQueue = MyCircularQueue(3)
# True
print(myCircularQueue.enQueue(1))
# True
print(myCircularQueue.enQueue(2))
# True
print(myCircularQueue.enQueue(3))
# False
print(myCircularQueue.enQueue(4))
# 3
print(myCircularQueue.Rear())
# True
print(myCircularQueue.isFull())
# True
print(myCircularQueue.deQueue())
# True
print(myCircularQueue.enQueue(4))
# 4
print(myCircularQueue.Rear())

# endregion

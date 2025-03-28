"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:
- void add(key): Inserts the value key into the HashSet.
- bool contains(key): Returns whether the value key exists in the HashSet or not.
- void remove(key): Removes the value key in the HashSet.If key does not exist in the HashSet, do nothing.
"""


# region Solution

class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        index = self._hash(key)

        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)

        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        return key in self.buckets[index]

    def _hash(self, key: int) -> int:
        return key % self.size


# endregion

# region Tests

myHashSet = MyHashSet()
# set = [1]
myHashSet.add(1)
# set = [1, 2]
myHashSet.add(2)
# return True
myHashSet.contains(1)
# return False, (not found)
myHashSet.contains(3)
# set = [1, 2]
myHashSet.add(2)
# return True
myHashSet.contains(2)
# set = [1]
myHashSet.remove(2)
# return False, (already removed)
myHashSet.contains(2)

# endregion

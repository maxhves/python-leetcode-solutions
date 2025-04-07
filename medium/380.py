"""
Implement the RandomizedSet object.
- RandomizedSet() Initializes the RandomizedSet object.
- bool insert(int val) Inserts an item val into th set if not present. Return true if the item was not present, false
  otherwise.
- bool remove(int val) Returns a random element from the current set of elements (it's guaranteed that at least one
  element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.
"""
import random


# region Solution

class RandomizedSet:

    def __init__(self):
        self.elements = []
        self.index_elements_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_elements_map:
            return False

        self.elements.append(val)
        self.index_elements_map[val] = len(self.elements) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_elements_map:
            return False

        last_index = len(self.elements) - 1
        val_index = self.index_elements_map[val]

        self.index_elements_map[self.elements[last_index]] = val_index
        self.elements[val_index] = self.elements[last_index]
        self.elements.pop()

        del self.index_elements_map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.elements)


# endregion

# region Tests

randomizedSet = RandomizedSet()
# True
print(randomizedSet.insert(1))
# False
print(randomizedSet.remove(2))
# True
print(randomizedSet.insert(2))
# 1 OR 2 (randomly)
print(randomizedSet.getRandom())
# True
print(randomizedSet.remove(1))
# False
print(randomizedSet.insert(2))
# 2
print(randomizedSet.getRandom())

# endregion

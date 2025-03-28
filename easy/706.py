"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:
- MyHashmap() initializes the object with an empty map.
- void put(int key, int value): inserts a (key, value) pair into the HashMap. If the key already exists in the map,
  update the corresponding value.
- int get(int key): returns the value to which the specified key is mapped, or -1 if this map contains no mapping for
  the key.
- void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
"""


# region Solution

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        bucket, index = self._get_index(key)

        if index < 0:
            bucket.append((key, value))
        else:
            bucket[index] = (key, value)

    def get(self, key: int) -> int:
        bucket, index = self._get_index(key)

        if index < 0:
            return -1
        else:
            return bucket[index][1]

    def remove(self, key: int) -> None:
        bucket, index = self._get_index(key)

        if index >= 0:
            bucket.remove(bucket[index])

    def _hash(self, key: int) -> int:
        return key % self.size

    def _get_index(self, key: int):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]

        for index, (bucket_key, bucket_value) in enumerate(bucket):
            if bucket_key == key:
                return bucket, index

        return bucket, -1


# endregion

# region Tests

myHashMap = MyHashMap()
# The map is now [[1, 1]]
myHashMap.put(1, 1)
# The map is now [[1, 1], [2, 2]]
myHashMap.put(2, 2)
# Return 1. The map is now [[1, 1], [2, 2]]
myHashMap.get(1)
# Return -1. The map is now [[1, 1], [2, 2]]
myHashMap.get(3)
# The map is now [[1, 1], [2, 1]]
myHashMap.put(2, 1)
# Return 1. The map is now [[1, 1], [2, 1]
myHashMap.get(2)
# Remove the mapping for 2. The map is now [[1, 1]]
myHashMap.remove(2)
# Return -1. The map is now [[1, 1]]
myHashMap.get(2)

# endregion

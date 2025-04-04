"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any
order.
"""
from collections import defaultdict
from typing import List


# region Solution

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    occurrences = defaultdict(int)
    frequencies = defaultdict(list)
    results = []

    # Occurrences of a particular element.
    for num in nums:
        occurrences[num] += 1

    # Frequencies of particular elements.
    for element, occurrences in occurrences.items():
        frequencies[occurrences].append(element)

    # Results based on k most frequent
    for frequency in range(len(nums), 0, -1):
        if frequency in frequencies:
            results.extend(frequencies[frequency])

            if len(results) >= k:
                return results[:k]

    return results


# endregion

# region Tests

# [3, 4]
print(top_k_frequent([3, 4, 5, 5], 2))

# [1, 2]
print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))

# [1]
print(top_k_frequent([1], 1))

# endregion

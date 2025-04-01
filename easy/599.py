"""
Given two arrays of strings list1 and list2, find the common strings with the least index sum.

A common string is a string that appeared in both list1 and list2.

A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j]
then i + j should be the minimum value among all the other common strings.

Return all the common strings with the least index sum. Return the answer in any order.
"""
from typing import List


# region Solution

def find_restaurant(list1: List[str], list2: List[str]) -> List[str]:
    list1_occurrences = {}
    min_index_sum = -1
    results = []

    for i in range(len(list1)):
        list1_occurrences[list1[i]] = i

    for i in range(len(list2)):
        current_element = list2[i]

        if current_element in list1_occurrences:
            index_sum = list1_occurrences[current_element] + i

            if min_index_sum == -1:
                min_index_sum = index_sum
                results.append(current_element)
            else:
                if index_sum == min_index_sum:
                    results.append(current_element)
                elif index_sum < min_index_sum:
                    results.clear()
                    results.append(current_element)
                    min_index_sum = index_sum

    return results


# endregion

# region Tests

# ["Shogun"]
print(find_restaurant(
    ["Shogun", "Tapioca Express", "Burger King", "KFC"],
    ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
))

# ["Shogun"]
print(find_restaurant(
    ["Shogun", "Tapioca Express", "Burger King", "KFC"],
    ["KFC", "Shogun", "Burger King"]
))

# ["sad", "happy"]
print(find_restaurant(
    ["happy", "sad", "good"],
    ["sad", "happy", "good"]
))

# endregion

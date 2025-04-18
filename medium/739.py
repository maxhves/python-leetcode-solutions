"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that
answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is
no future day for which this is possible, keep answer[i] == 0 instead.
"""
from typing import List


# region Solution


def daily_temperatures(temperatures: List[int]) -> List[int]:
    days_to_warmer = [0] * len(temperatures)
    temp_index_stack = []

    for i in range(len(temperatures)):
        while temp_index_stack and temperatures[i] > temperatures[temp_index_stack[-1]]:
            top_index = temp_index_stack.pop()
            days_to_warmer[top_index] = i - top_index

        temp_index_stack.append(i)

    return days_to_warmer


# endregion

# region Tests

# [1, 1, 4, 2, 1, 1, 0, 0]
print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))

# [1, 1, 1, 0]
print(daily_temperatures([30, 40, 50, 60]))

# [1, 1, 0]
print(daily_temperatures([30, 60, 90]))

# endregion

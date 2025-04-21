"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer
in nums and then concatenate all the integers.
- For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build
  the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.
"""
from typing import List


# region Solution

def find_target_sum_ways(nums: List[int], target: int) -> int:
    cache = {}

    def dfs(index: int, current_sum: int) -> int:
        if (index, current_sum) in cache:
            return cache[(index, current_sum)]

        if index == len(nums):
            return 1 if current_sum == target else 0

        cache[(index, current_sum)] = (
                dfs(index + 1, current_sum + nums[index]) +
                dfs(index + 1, current_sum - nums[index])
        )

        return cache[(index, current_sum)]

    return dfs(0, 0)


# endregion

# region Tests

# 5
print(find_target_sum_ways([1, 1, 1, 1, 1], 3))

# 1
print(find_target_sum_ways([1], 1))

# endregion

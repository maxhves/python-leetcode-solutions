"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith customer has in the
jth bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer
that has the maximum wealth.
"""

from typing import List


# region Solution

def maximum_wealth(accounts: List[List[int]]) -> int:
    max_wealth = 0

    for bank in accounts:
        wealth = 0
        for account in bank:
            wealth += account

        max_wealth = max(max_wealth, wealth)

    return max_wealth


# endregion

# region Tests

# 6
print(maximum_wealth([[1, 2, 3], [3, 2, 1]]))

# 10
print(maximum_wealth([[1, 5], [7, 3], [3, 5]]))

# endregion

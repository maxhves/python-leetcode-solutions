"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]...nums[i]).

Return the running sum of nums.
"""

from typing import List

#region Solution

def running_sum(nums: List[int]) -> List[int]:
    # TODO: Solution incoming...
    return [0, 1, 2, 3, 4]


#endregion

#region Tests

# Expected: [1,3,6,10]
print(running_sum([1, 2, 3, 4]))

# Expected: [1,2,3,4,5]
print(running_sum([1, 1, 1, 1, 1]))

# Expected: [3,4,6,16,17]
print(running_sum([3, 1, 2, 10, 1]))

#endregion

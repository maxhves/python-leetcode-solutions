"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose
sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""
from typing import List


# region Solution

def min_sub_array_len(target: int, nums: List[int]) -> int:
    left = 0
    right = 0

    min_valid_window_size = 0
    current_window_sum = nums[0]
    current_window_length = 1

    # If the single window matches target, just return it.
    if current_window_sum >= target:
        return current_window_length
    elif len(nums) == 1:
        return 0
    else:
        # Just increment right immediately, we know the single window isn't enough.
        right += 1
        current_window_sum += nums[right]
        current_window_length += 1

    # Iterate over every item in the array.
    while left < right:
        # Valid window
        if current_window_sum >= target:
            if min_valid_window_size == 0:
                min_valid_window_size = current_window_length
            else:
                min_valid_window_size = min(min_valid_window_size, current_window_length)

            # Decrease the window size on the left
            current_window_sum -= nums[left]
            left += 1
            current_window_length -= 1
        else:
            # Sum is too small, increase right
            if right < len(nums) - 1:
                right += 1
                current_window_sum += nums[right]
                current_window_length += 1
            else:
                # If right is at the end, all we can do is increase left.
                current_window_sum -= nums[left]
                left += 1
                current_window_length -= 1

    return 1 if current_window_sum >= target else min_valid_window_size


# endregion

# region Tests

# 2
print(min_sub_array_len(7, [2, 3, 1, 2, 4, 3]))

# 1
print(min_sub_array_len(4, [1, 4, 4]))

# 0
print(min_sub_array_len(11, [1, 1, 1, 1, 1, 1, 1, 1]))

# endregion

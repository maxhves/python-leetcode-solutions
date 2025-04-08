"""
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each
move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of dead ends, meaning if the lock displays and of these codes, the wheels of the lock will stop
turning, and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns
required to open the lock, or -1 if it is impossible.
"""
from collections import deque
from typing import List


# region Solution

def open_lock(dead_ends: List[str], target: str) -> int:
    visited_states = set(dead_ends)

    if "0000" in visited_states:
        return -1

    state_queue = deque()
    state_queue.append(("0000", 0))  # State | Turns

    def get_next_states(state: str) -> List[str]:
        child_states = []

        for i in range(4):
            plus_one_char = str((int(state[i]) + 1) % 10)
            minus_one_char = str(((int(state[i]) - 1) + 10) % 10)

            child_states.append(state[:i] + plus_one_char + state[i + 1:])
            child_states.append(state[:i] + minus_one_char + state[i + 1:])

        return child_states

    while state_queue:
        current_state = state_queue.popleft()

        if current_state[0] == target:
            return current_state[1]

        next_states = get_next_states(current_state[0])
        for next_state in next_states:
            if next_state not in visited_states:
                visited_states.add(next_state)
                state_queue.append((next_state, current_state[1] + 1))

    return -1


# endregion

# region Tests

# 6
print(open_lock(["0201", "0101", "0102", "1212", "2002"], "0202"))

# 1
print(open_lock(["8888"], "0009"))

# -1
print(open_lock(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"))

# endregion

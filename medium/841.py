"""
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to
visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which
room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return
true if you can visit all the rooms, or false otherwise.
"""
from typing import List


# Recursively visit each element and store the keys we find.
# Process the keys, visiting the rooms it unlocks.
# Store keys in a set.
# Ultimately check if the set is the length of the rooms array.

# region Solution

def can_visit_all_rooms(rooms: List[List[int]]) -> bool:
    found_keys = set()
    room_check_queue = [0]

    while room_check_queue:
        next_key = room_check_queue.pop()
        found_keys.add(next_key)

        for key in rooms[next_key]:
            if key not in found_keys:
                room_check_queue.append(key)
                found_keys.add(key)

    return len(found_keys) == len(rooms)


# endregion

# region Tests

# True
print(can_visit_all_rooms([[1], [2], [3], []]))

# False
print(can_visit_all_rooms([[1, 3], [3, 0, 1], [2], [0]]))

# endregion

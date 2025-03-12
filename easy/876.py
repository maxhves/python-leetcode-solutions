"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""
from typing import Optional

from common.list_node import ListNode, create_linked_list, linked_list_to_string


# region Solution

# 1. Count the number of nodes.
# 2. Divide the count by 2 (round up if necessary).
# 3. Iterate over the nodes again, and retrieve the desired node.
# OR
# 3. In the initial iteration, store each node in an array for quick retrival later.

# 1. Iterate over the linked list with two nodes.
# 2. Whilst the next node isn't null, increase one pointer by one and the other by two.
# 3. Halfway will be the value of the first pointer.

def middle_node_count(head: Optional[ListNode]) -> Optional[ListNode]:
    count = 0
    nodes = []
    current_node = head

    while current_node is not None:
        count += 1
        nodes.append(current_node)
        current_node = current_node.next

    return nodes[count // 2]


def middle_node_pointer(head: Optional[ListNode]) -> Optional[ListNode]:
    middle_node = head
    end_node = head

    while end_node and end_node.next:
        middle_node = middle_node.next
        end_node = end_node.next.next

    return middle_node


# endregion

# region Tests

# [3, 4, 5]
case_one = create_linked_list([1, 2, 3, 4, 5])
print(linked_list_to_string(middle_node_count(case_one)))
print(linked_list_to_string(middle_node_pointer(case_one)))

# [4, 5, 6]
case_two = create_linked_list([1, 2, 3, 4, 5, 6])
print(linked_list_to_string(middle_node_count(case_two)))
print(linked_list_to_string(middle_node_pointer(case_two)))

# endregion

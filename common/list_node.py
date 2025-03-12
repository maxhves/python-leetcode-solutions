class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def linked_list_to_string(head):
    return " -> ".join(map(str, iter_linked_list(head))) + " -> None"


def iter_linked_list(head):
    while head:
        yield head.val
        head = head.next

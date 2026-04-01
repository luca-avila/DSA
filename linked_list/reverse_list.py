from list_node import ListNode

def reverse_list(head: ListNode | None) -> ListNode | None:
    # Complexity O(n)
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev
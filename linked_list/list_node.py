from __future__ import annotations

class ListNode:
    def __init__(self, value: int = 0, next: ListNode | None = None):
        self.value = value
        self.next = next

    def __repr__(self):
        next_value = self.next.value if self.next else None
        return f"ListNode(value={self.value}, next={next_value})"
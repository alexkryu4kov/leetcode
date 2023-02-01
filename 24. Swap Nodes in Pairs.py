from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = head.next
        prev = None
        while head and head.next:
            if prev:
                prev.next = head.next
            prev = head

            next_node = head.next.next
            head.next.next = head

            head.next = next_node
            head = next_node

        return dummy


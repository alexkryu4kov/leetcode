from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next is None:
            return head
        curr = head
        count = 0
        while count < left - 1:
            curr = curr.next
            count += 1
        before_left = curr
        while count < right:
            curr = curr.next
            count += 1
        before_right = curr
        after_right = before_right.next
        prev = after_right
        curr = before_left.next
        while curr and curr != after_right:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        before_left.next = prev

        return head


head = ListNode(1)


sol = Solution()
l = sol.reverseBetween(head, 1, 2)
print(l.val)

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


head = ListNode(3)
head.next = ListNode(2)
head.next = ListNode(0)
head.next = ListNode(-4)
sol = Solution()
print(sol.hasCycle(head))

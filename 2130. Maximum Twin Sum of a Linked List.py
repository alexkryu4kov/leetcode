from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        max_sum = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        while prev:
            max_sum = max(max_sum, head.val + prev.val)
            prev = prev.next
            head = head.next
        return max_sum


head = ListNode(0)
second = ListNode(1)
third = ListNode(2)
head.next = second
second.next = third

sol = Solution()
print(sol.pairSum(head))

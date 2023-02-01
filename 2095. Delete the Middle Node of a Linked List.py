from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        size = 0
        while dummy:
            dummy = dummy.next
            size += 1
        middle = int(size / 2)
        size = 0
        dummy = head
        prev_node = None
        next_node = None
        while dummy:
            if size == middle - 1:
                prev_node = dummy
            if size == middle + 1:
                next_node = dummy
                break
            dummy = dummy.next
            size += 1
        if not prev_node:
            return None
        if next_node:
            prev_node.next = next_node
        else:
            prev_node.next = None
        return head


head = ListNode(0)
second = ListNode(1)
third = ListNode(2)
head.next = second
second.next = third

sol = Solution()
print(sol.deleteMiddle(head))

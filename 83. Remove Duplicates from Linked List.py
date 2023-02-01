from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        dummy = head
        prev = dummy
        dummy = dummy.next
        while dummy:
            if prev.val == dummy.val:
                prev.next = dummy.next
                dummy = dummy.next
            else:
                prev = dummy
                dummy = dummy.next
        return head


head = ListNode(1)
second = ListNode(1)
third = ListNode(1)
head.next = second
second.next = third


sol = Solution()
print(sol.deleteDuplicates(head))

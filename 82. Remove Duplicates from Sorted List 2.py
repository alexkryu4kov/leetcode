from collections import defaultdict
from copy import deepcopy
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash_map = defaultdict(int)
        dummy = head
        counts = 0
        while dummy:
            hash_map[dummy.val] += 1
            dummy = dummy.next
            counts += 1
        dummy = head
        print(hash_map)
        new_head = None
        while dummy:
            if hash_map[dummy.val] < 2:
                print(dummy.val)
                if new_head:
                    current = new_head
                    while current.next:
                        current = current.next
                    current.next = deepcopy(dummy)
                    current.next.next = None
                else:
                    new_head = deepcopy(dummy)
                    new_head.next = None
            dummy = dummy.next
        return new_head


head = ListNode(1)
second = ListNode(1)
third = ListNode(1)
head.next = second
second.next = third


sol = Solution()
print(sol.deleteDuplicates(head))

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        answer = []
        queue = deque([root])

        while queue:
            nodes_in_current_level = len(queue)
            answer.append(queue[-1].val)
            for _ in range(nodes_in_current_level):

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return answer


first = TreeNode(val=1)
second = TreeNode(val=2)
third = TreeNode(val=3)
fourth = TreeNode(val=4)
fifth = TreeNode(val=5)
sixth = TreeNode(val=6)
first.left = second
first.right = third
second.left = fourth
third.right = fifth
third.left = sixth

print_all_nodes(first)

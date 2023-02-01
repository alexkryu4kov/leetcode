from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])

        while queue:
            answer = 0
            nodes_in_current_level = len(queue)
            for _ in range(nodes_in_current_level):
                node = queue.popleft()
                answer += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return answer

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        answer = []
        queue = deque([root])

        while queue:
            tmp = float('-inf')
            nodes_in_current_level = len(queue)
            for _ in range(nodes_in_current_level):
                node = queue.popleft()
                tmp = max(tmp, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            answer.append(tmp)

        return answer

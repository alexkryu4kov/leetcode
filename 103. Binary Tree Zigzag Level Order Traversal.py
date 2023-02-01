from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque([root])

        answer = []
        level = -1

        while queue:

            tmp_answer = []
            nodes_in_current_level = len(queue)

            for _ in range(nodes_in_current_level):
                node = queue.popleft()
                tmp_answer.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1
            if level % 2 == 1:
                tmp_answer.reverse()
            answer.append(tmp_answer)
        return answer

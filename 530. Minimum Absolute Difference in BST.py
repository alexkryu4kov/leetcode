from itertools import starmap
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return []
            left = dfs(node.left)
            right = dfs(node.right)
            return left + [node.val] + right

        values = dfs(root)

        return min([j-i for i, j in zip(values[:-1], values[1:])])

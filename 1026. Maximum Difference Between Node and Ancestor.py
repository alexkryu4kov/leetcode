from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = [0]
        if root is None:
            return 0
        self.dfs(root, root.val, root.val, res)
        return res[0]

    def dfs(self, root: Optional[TreeNode], low: int, high: int, result: list[int]) -> int:
        if not root:
            return 0
        result[0] = max(result[0], abs(low - root.val), abs(high - root.val))
        mi = min(root.val, low)
        ma = max(root.val, high)
        self.dfs(root.left, mi, ma, result)
        self.dfs(root.right, mi, ma, result)


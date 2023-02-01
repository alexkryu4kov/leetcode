from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root, 0, targetSum)

    def dfs(self, node: Optional[TreeNode], curr: int, targetSum: int) -> bool:
        if not node:
            return False

        if not node.left and not node.right:
            return (curr + node.val) == targetSum

        curr += node.val
        left = self.dfs(node.left, curr, targetSum)
        right = self.dfs(node.right, curr, targetSum)
        return left or right

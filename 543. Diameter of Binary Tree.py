from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Для каждого root найти максимальную глубину для root.left и root.right.
        Найти максимум из глубины (root.left, root.right).
        """

        res = [0]
        self.search_max(root, res)
        return res[0] - 1

    def search_max(self, root: Optional[TreeNode], res):
        if not root:
            return 0

        left = self.search_max(root.left, res)
        right = self.search_max(root.right, res)

        res[0] = max(res[0], left + right + 1)
        return 1 + max(left, right)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.is_good_node(root, float('-inf'))

    def is_good_node(self, node: TreeNode, max_value) -> int:
        if not node:
            return 0
        left = self.is_good_node(node.left, max(max_value, node.val))
        right = self.is_good_node(node.right, max(max_value, node.val))
        answer = left + right
        if node.val >= max_value:
            answer += 1
        return answer

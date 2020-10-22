class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        def traverse(node, i):
            if node.left is None and node.right is None:
                return i
            if node.left and node.right:
                return min(traverse(node.left, i + 1), traverse(node.right, i + 1))
            if node.left:
                return traverse(node.left, i + 1)
            if node.right:
                return traverse(node.right, i + 1)
        return traverse(root, 1)

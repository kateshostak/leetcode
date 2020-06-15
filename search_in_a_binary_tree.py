class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        def traverse(node):
            if not node:
                return None

            if val == node.val:
                return node

            if val < node.val:
                return traverse(node.left)
            else:
                return traverse(node.right)

        return traverse(root)

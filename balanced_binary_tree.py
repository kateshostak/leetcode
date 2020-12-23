class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.bal = True

        def traverse(node, i):
            if node is None:
                return i

            l = traverse(node.left, i + 1)
            r = traverse(node.right, i + 1)
            if abs(l - r) > 1:
                self.bal = False
            return max(l, r)
        traverse(root, 0)
        return self.bal

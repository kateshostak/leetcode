class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.head = None
        self.tmp = None

        def traverse(node):
            if not node:
                return
            traverse(node.left)
            if not self.head:
                self.head = node
                self.head.left = None

                self.tmp = self.head
            else:
                self.tmp.right = node
                self.tmp.left = None
                self.tmp = self.tmp.right
            traverse(node.right)

        traverse(root)
        self.tmp.right = None
        self.tmp.left = None
        return self.head

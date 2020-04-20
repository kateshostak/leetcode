# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        def add_node(root, val):
            tmp = TreeNode(val)
            curr = root
            while True:
                if val < curr.val:
                    if curr.left is None:
                        curr.left = tmp
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = tmp
                        break
                    else:
                        curr = curr.right
        for val in preorder[1:]:
            add_node(root, val)
        return root

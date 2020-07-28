from typing import List
import pdb

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        postorder.reverse()
        root_val = postorder[0]
        root_val_ind = inorder.index(root_val)
        left_val = -1
        if root_val_ind != 0:
            left_val = inorder[root_val_ind - 1]
            left_ind = postorder.index(left_val)

        def traverse(i, j):
            if i >= j:
                return None
            node = TreeNode(postorder[i])
            node.left = traverse(i*2 + 1, j)
            node.right = traverse(i*2, j)
            return node
        root = TreeNode(root_val)
        if left_val != -1:
            root.right = traverse(1, left_ind)
            root.left = traverse(left_ind, len(postorder))
        else:
            root.right = traverse(1, len(postorder))
        return root

    def inorder(self, root):
        res = []

        def traverse(node):
            if not node:
                return
            traverse(node.left)
            res.append(node.val)
            traverse(node.right)
        traverse(root)
        return res


def main():
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    root = Solution().buildTree(inorder, postorder)
    print(Solution().inorder(root))


if __name__ == '__main__':
    main()

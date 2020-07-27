from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def traverse(i):
            if i > len(postorder):
                return None
            node = TreeNode(postorder[i])
            node.left = traverse(i*2 + 1)
            node.right = traverse(i*2 + 2)
            return node
        root = traverse(0)
        print(self.inorder(root))

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
    postorder = [9, 15, 7, 20, 3]
    Solution().buildTree(postorder)


if __name__ == '__main__':
    main()

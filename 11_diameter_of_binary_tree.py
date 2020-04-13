import pdb


class TreeNode:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        tree = [root.x]
        def traverse(node):
            if not node:
                return
            if node.left:
                tree.append(node.left.x)
            if node.right:
                tree.append(node.right.x)
            traverse(node.right)
            traverse(node.left)
        traverse(root)
        return tree

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(7)
    s = Solution()
    res = s.diameterOfBinaryTree(root)
    print(res)


if __name__ == '__main__':
    main()

class TreeNode:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 1

        def traverse(node):
            if not node:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            self.diameter = max(left + right + 1, self.diameter)
            return max(left, right) + 1
        traverse(root)
        return self.diameter - 1


def main():
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    # Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(Solution().diameterOfBinaryTree(root))


if __name__ == '__main__':
    main()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def traverse(node):
            if not node:
                return 0
            s1 = traverse(node.left)
            s2 = traverse(node.right)
            return max(s1 + node.val, s2 + node.val, node.val + s1 + s2, node.val)

        max_ = traverse(root)
        return(max_)


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().maxPathSum(root))


if __name__ == '__main__':
    main()

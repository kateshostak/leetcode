class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        sums = []
        def traverse(node):
            if not node:
                return 0
            s1 = traverse(node.left)
            s2 = traverse(node.right)
            sums.append(node.val + s1 + s2)
            max_ = max(s1 + node.val, s2 + node.val, node.val)
            sums.append(max_)
            return max_
        m_ = traverse(root)
        return(max(sums))


def main():
    # arr = [1, 2, 3]
    # out = 6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().maxPathSum(root))

    # arr = [-10,9,20,null,null,15,7]
    # out = 42
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().maxPathSum(root))

    # arr = [5,4,8,11,null,13,4,7,2,null,null,null,1]
    # out = 48
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    print(Solution().maxPathSum(root))


if __name__ == '__main__':
    main()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []

        def traverse(node):
            if not node:
                return
            traverse(node.left)
            res.append(node.val)
            traverse(node.right)

        traverse(root)
        return res[k - 1]


def main():
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(4)
    k = 1
    res = Solution().kthSmallest(root, k)
    print(f'expected::1 got::{res}')

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    root.right = TreeNode(6)
    k = 3
    res = Solution().kthSmallest(root, k)
    print(f'expected::3 got::{res}')

    root = TreeNode(2)
    root.left = TreeNode(1)
    k = 2
    res = Solution().kthSmallest(root, k)
    print(f'expected::2 got::{res}')


if __name__ == '__main__':
    main()

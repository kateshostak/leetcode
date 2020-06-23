class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        self.i = 0
        def traverse(node, i):
            if not node:
                return
            self.i += 1
            traverse(node.left, i)
            traverse(node.right, i)

        traverse(root, 0)
        return self.i

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)

    res = Solution().countNodes(root)
    print(f'expected::6, got::{res}')


if __name__ == '__main__':
    main()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def traverse(node, i):
            i += 1
            if node.left:
                return traverse(node.left, i)
            elif node.right:
                return traverse(node.right, i)
            else:

                return i

        return traverse(root, 0)


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

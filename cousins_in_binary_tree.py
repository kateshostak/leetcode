from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        d = defaultdict(int)

        def traverse(node, parent, i):
            if not node:
                return
            print(f'node::{node.val}, i::{i}')
            if node.val == x or node.val == y:
                d[parent.val] = i
                return

            traverse(node.left, node, i + 1)
            traverse(node.right, node, i + 1)

        traverse(root, None, 0)
        print(d.items())
        if len(d) < 2:
            return False


        if d.popitem()[1] == d.popitem()[1]:
            return True
        return False


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right = TreeNode(3)
    x = 3
    y = 4
    res = Solution().isCousins(root, x, y)
    print(f'expected::False, got::{res}')

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right = TreeNode(3)
    root.right.right = TreeNode(5)
    x = 5
    y = 4
    res = Solution().isCousins(root, x, y)
    print(root.val)
    print(f'expected::True, got::{res}')

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right = TreeNode(3)
    x = 2
    y = 3
    res = Solution().isCousins(root, x, y)
    print(f'expected::False, got::{res}')


if __name__ == '__main__':
    main()

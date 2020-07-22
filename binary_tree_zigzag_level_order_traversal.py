from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        d = {}

        def traverse(node, i):
            if not node:
                return
            if i not in d:
                d[i] = []
            if i % 2 == 0:
                d[i].append(node.val)
            else:
                d[i].insert(0, node.val)
            traverse(node.left, i + 1)
            traverse(node.right, i + 1)
        traverse(root, 0)
        return [d[key] for key in d]


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    res = Solution().zigzagLevelOrder(root)
    print(f'expected::[[3], [20, 9], [15, 7]], got::{res}')


if __name__ == '__main__':
    main()

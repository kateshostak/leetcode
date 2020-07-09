from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        d = defaultdict(list)

        def traverse(node, i, j):
            d[j].append(i)
            if node.left:
                traverse(node.left, i*2, j + 1)
            if node.right:
                traverse(node.right, i*2 + 1, j + 1)
            return
        traverse(root, 1, 1)
        max_ = 1
        for _, elem in d.items():
            max_ = max(max_, elem[-1] - elem[0] + 1)
        return max_


def main():
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right = TreeNode(2)
    root.right.right = TreeNode(9)
    res = Solution().widthOfBinaryTree(root)
    print(f'expected::4, got::{res}')


if __name__ == '__main__':
    main()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.sum_ = 0

        def traverse(node, curr_number):
            curr_number = 10 * curr_number + node.val
            if node.left:
                traverse(node.left, curr_number)
            if node.right:
                traverse(node.right, curr_number)
            if not(node.right or node.left):
                self.sum_ += curr_number
                return
        if root:
            traverse(root, 0)
        return self.sum_


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    res = Solution().sumNumbers(root)
    print(f'expected::25, got::{res}')


if __name__ == '__main__':
    main()

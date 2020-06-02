class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def traverse(node):
            if not node:
                return
            node.left, node.right = traverse(node.right), traverse(node.left)
            return node
        return traverse(root)

    def as_arr(self, root):
        res = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            res.append(node.val)
            if node.right:
                traverse(node.right)
            return

        traverse(root)
        return res


def main():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    sol = Solution()
    tree = sol.as_arr(root)
    res = sol.as_arr(sol.invertTree(root))
    tree.reverse()
    print(f'expected:{tree}, got::{res}')


if __name__ == '__main__':
    main()

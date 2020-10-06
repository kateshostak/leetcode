class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def traverse(node):
            if not node:
                return TreeNode(val)

            if val < node.val:
                node.left = traverse(node.left)
            else:
                node.right = traverse(node.right)
            return node

        return traverse(root)

    def print_(self, node):
        def traverse(node):
            if not node:
                return

            traverse(node.left)
            print(node.val)
            traverse(node.right)
        traverse(node)


def main():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    val = 5
    tree = Solution()
    tree.insertIntoBST(root, val)
    tree.print_(root)


if __name__ == '__main__':
    main()

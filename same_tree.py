class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def traverse(node1, node2):
            if node1.val != node2.val:
                return False

            if node1.right and node2.right:
                traverse(node1.right, node2.right)
            elif node1.right or node2.right:
                return False

            if node1.left and node2.left:
                traverse(node1.left, node2.left)
            elif node1.left or node2.left:
                return False

            return True

        return traverse(p, q)


def tree_maker():
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    return p


def main():
    p, q = tree_maker(), tree_maker()
    res = Solution().isSameTree(p, q)
    print(f'expected::True, got::{res}')


if __name__ == '__main__':
    main()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def traverse(node1, node2):
            if not node1 and not node2:
                return True

            if not node1 and node2:
                return False

            if node1 and not node2:
                return False

            if node1.val != node2.val:
                return False

            if not traverse(node1.right, node2.right):
                return False

            if not traverse(node1.left, node2.left):
                return False

            return True

        return traverse(p, q)


def main():
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)

    q = TreeNode(1)
    q.left = TreeNode(1)
    q.right = TreeNode(2)

    res = Solution().isSameTree(p, q)
    print(f'expected::False, got::{res}')


if __name__ == '__main__':
    main()

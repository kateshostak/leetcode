class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def traverse(node):
            if node is None:
                return 0, 0

            tilt_l, sum_l = traverse(node.left)
            tilt_r, sum_r = traverse(node.right)
            return abs(sum_l - sum_r) + tilt_l + tilt_r, node.val + sum_l + sum_r

        return(traverse(root)[0])


def tree_from_arr(arr):
    if len(arr) == 0:
        return None

    root = TreeNode(arr[0])

    def traverse(tmp, i):
        if i >= len(arr)//2:
            return None
        try:
            val = arr[i*2 + 1]
            if val is None:
                val = 0
            tmp.left = TreeNode(val)
        except IndexError:
            pass

        try:
            val = arr[i*2 + 2]
            if val is None:
                val = 0
            tmp.right = TreeNode(val)
        except IndexError:
            pass
        print(f'node::{tmp.val}, left::{tmp.left.val}, right::{tmp.right.val}')
        traverse(tmp.left, i*2 + 1)
        traverse(tmp.right, i*2 + 2)
        return tmp

    return traverse(root, 0)


def as_arr(root):

    def traverse(node):
        if node is None:
            return
        print(node.val, end=' ')
        traverse(node.left)
        traverse(node.right)
    traverse(root)


def main():
    root = tree_from_arr([4, 2, 9, 3, 5, None, 7])
    as_arr(root)
    res = Solution().findTilt(root)
    print(f'expected::15, got::{res}')


if __name__ == '__main__':
    main()

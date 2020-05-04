from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:

        def traverse(node, i):
            if not node:
                return False

            if not node.left and not node.right:
                if arr[i] == node.val and i == len(arr) - 1:
                    return True
            else:
                if i < len(arr) - 1 and arr[i] == node.val:
                    if traverse(node.left, i + 1):
                        return True
                    return traverse(node.right, i + 1)
            return False

        return traverse(root, 0)


def main():
    # root = [0,1,0,0,1,0,null,null,1,0,0]
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.left.right = TreeNode(1)
    root.left.right = TreeNode(1)
    root.left.right.left = TreeNode(0)
    root.left.right.right = TreeNode(0)
    root.right = TreeNode(0)
    root.right.left = TreeNode(0)

    arr = [0, 1, 0, 1]
    res = (Solution().isValidSequence(root, arr))
    print(f'expected: true, got:{res}')

    arr = [0, 0, 1]
    res = (Solution().isValidSequence(root, arr))
    print(f'expected: false, got:{res}')

    arr = [0, 1, 1]
    res = (Solution().isValidSequence(root, arr))
    print(f'expected: false, got:{res}')

    arr = [0, 1, 0, 0]
    res = (Solution().isValidSequence(root, arr))
    print(f'expected: false, got:{res}')

    arr = [0, 0, 0]
    res = (Solution().isValidSequence(root, arr))
    print(f'expected: true, got:{res}')


if __name__ == '__main__':
    main()

from typing import List
import pdb


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        self.isValid = False

        def traverse(node, i):
            if not node:
                self.isValid = True
                return
            else:
                if i < len(arr) - 1 and arr[i] == node.val:
                    traverse(node.left, i + 1)
                    traverse(node.right, i + 1)
                else:
                    return
        traverse(root, 0)
        return  self.isValid


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
    # out = true
    arr = [0, 0, 1]
    # out = false
    arr = [0, 1, 1]
    # out = false
    arr = [0, 1, 0, 0]
    # out = true
    arr = [0, 0, 0]
    # out = true
    print(Solution().isValidSequence(root, arr))

    # tree = [8,null,5,4,null,4]
    # arr = [8]
    # out = false
    root = TreeNode(8)
    root.right = TreeNode(5)
    print(Solution().isValidSequence(root, arr))
    arr = [8]
if __name__ == '__main__':
    main()

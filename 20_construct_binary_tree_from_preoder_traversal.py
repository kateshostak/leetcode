from typing import List
import pdb


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return self.val


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        print(f'len = {len(preorder)}')
        pdb.set_trace()

        def traverse(grandparent, parent, i):
            if grandparent:
                print(f'i:{i}')
                if i > len(preorder) - 1 or preorder[i] > grandparent.val:
                    print('out')
                    return


            if preorder[i] > parent.val:
                parent.right = TreeNode(preorder[i])
                traverse(parent, parent.right, i + 1)
            else:
                parent.left = TreeNode(preorder[i])
                traverse(parent, parent.left, i + 1)
            traverse(grandparent, parent, i + 1)
        traverse(None, root, 1)
        return root


def main():
    arr = [8, 5, 1, 7, 10, 12]
    print(Solution().bstFromPreorder(arr))


if __name__ == '__main__':
    main()

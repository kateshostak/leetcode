class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        self.s = ''

        def traverse(node):
            if node is None:
                return

            self.s += str(node.val)
            self.s += ' '
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        print(f's::{self.s}')
        return self.s

    def deserialize(self, data: str) -> TreeNode:
        tmp = data.split(' ')
        self.root = TreeNode(tmp[0])

        def add_node(val):
            curr = self.root
            while True:
                if val < curr.val:
                    if curr.left is None:
                        curr.left = TreeNode(val)
                        break
                    curr = curr.left

                else:
                    if curr.right is None:
                        curr.right = TreeNode(val)
                        break
                    curr = curr.right
        for i in range(1, len(tmp)):
            add_node(tmp[i])

        return self.root


def preorder(root):
    def traverse(node):
        if node is None:
            return
        print(node.val, end=' ')
        traverse(node.left)
        traverse(node.right)
    traverse(root)


def main():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    ser = Codec()
    deser = Codec()
    tree_str = ser.serialize(root)
    ans_root = deser.deserialize(tree_str)
    preorder(ans_root)


if __name__ == '__main__':
    main()

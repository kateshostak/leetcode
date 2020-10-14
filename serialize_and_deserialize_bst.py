class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        if root is None:
            return ''

        self.s = ''

        def traverse(node):
            if node is None:
                return

            self.s += str(node.val)
            self.s += ' '
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        print(self.s)
        return self.s

    def deserialize(self, data: str) -> TreeNode:
        if len(data) == 0:
            return []

        tmp = data.strip().split(' ')
        self.root = TreeNode(int(tmp[0]))

        def add_node(node, val):
            if not node:
                return TreeNode(val)
            if val < node.val:
                node.left = add_node(node.left, val)
            else:
                node.right = add_node(node.right, val)
            return node

        for i in range(1, len(tmp)):
            add_node(self.root, int(tmp[i]))

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
    root = TreeNode(41)
    root.left = TreeNode(37)
    root.left.right = TreeNode(39)
    root.left.left = TreeNode(24)
    root.left.left.right = TreeNode(35)
    root.left.left.left = TreeNode(1)
    root.left.left.left.left = TreeNode(0)
    root.left.left.left.right = TreeNode(2)
    root.left.left.left.right.right = TreeNode(4)
    root.left.left.left.right.right.right = TreeNode(9)
    root.left.left.left.right.right.left = TreeNode(3)
    root.left.left.left.right.right.right.left = TreeNode(7)

    root.right = TreeNode(44)
    root.right.left = TreeNode(42)
    root.right.left.right = TreeNode(43)
    root.right.right = TreeNode(48)
    ser = Codec()
    deser = Codec()
    tree_str = ser.serialize(root)
    ans_root = deser.deserialize(tree_str)
    preorder(ans_root)


if __name__ == '__main__':
    main()

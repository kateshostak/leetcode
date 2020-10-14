class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:

        self.tmp = []

        def traverse(self, node):
            if node is None:
                return

            self.tmp.append(node.val)
            traverse(node.left)
            traverse(node.right)

        s = ''
        for elem in self.tmp:
            s += str(elem) + ' '

        return s

    def deserialize(self, data: str) -> TreeNode:
        tmp = data.split(' ')
        self.root = tmp[0]

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

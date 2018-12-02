class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.left_node = None
        self.right_node = None
    def insert_left_node(self, data):
        if self.left_node is None:
            self.left_node = BinaryTree(data)
        else:
            new_node = BinaryTree(data)
            new_node.left_node = self.left_node
            self.left_node = new_node
    def insert_right_node(self, data):
        if self.right_node is None:
            self.right_node = BinaryTree(data)
        else:
            new_node = BinaryTree(data)
            new_node.right_node = self.right_node
            self.right_node = new_node
    def get_right_node(self):
        return self.right_node
    def get_left_node(self):
        return self.left_node
    def set_root(self, root):
        self.root = root
    def get_root(self):
        return self.root
b = BinaryTree(0)
b.insert_left_node(1)
b.insert_right_node(10)
print(b.left_node.root)
print(b.right_node.root)
print(b.get_root())
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

# Binary Tree Traversal
def preorder(tree):
    if tree:
        print(tree.key)
        preorder(tree.left)
        preorder(tree.right)

def inorder(tree):
    if tree:
        inorder(tree.left)
        print(tree.key)
        inorder(tree.right)

def postorder(tree):
    if tree:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.key)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Pre-order")
preorder(root)
print("In-order")
inorder(root)
print("Post-order")
postorder(root)
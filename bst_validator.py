import sys

class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

def bst_validator(root, min=-sys.maxsize-1, max = sys.maxsize):
    if root is None:
        return True
    if (root.value > min and root.value < max and
        bst_validator(root.left, min, root.value) and
        bst_validator(root.right, root.value, max)):
        return True
    else:
        return False

root = Node(5)
l = Node(10)
r = Node(12)
rr = Node(15)
r.right = rr
root.left = l
root.right = r
print(bst_validator(root))
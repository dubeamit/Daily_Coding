# Given the root to a binary tree, count the total number of nodes there are.
# BASE CASE: if node null return 0; elif node == leaf node return 1
# RECURSIVE CASE: just add the count of the nodes in left and nodes in right

class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

def count(node):
    return count(node.left) + count(node.right) + 1 if node else 0

a = Node(2)
b = Node(1)
c = Node(0)
d = Node(5)
e = Node(7)
a.left = b
b.left = c
a.right = d
d.right = e
print(count(a))
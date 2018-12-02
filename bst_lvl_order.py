class Node:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

def bst_lvl_order_travs(node): 
    print()
    queue = [node] if node else []
    while queue:
        temp_node = queue.pop()
        print(temp_node.root, end = " ")
        if temp_node.left:
            queue.insert(0, temp_node.left)
        if temp_node.right:
            queue.insert(0, temp_node.right)
    print('\n')
# elements inserted as BST
a = Node(3)
b = Node(2)
c = Node(1)
d = Node(5)
e = Node(4)
f = Node(7)
a.left = b
b.left = c
a.right = d
d.left = e
d.right = f

bst_lvl_order_travs(a)
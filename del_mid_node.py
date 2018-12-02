class Node:
    def __init__(self, value = None):
        self.next = None
        self.value = value

def del_mid_node(node):
    if node is None or node.next is None:
        node = None
        return node
    slow = node
    fast = node
    prev = node
    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next
    prev.next = slow.next
    slow = None
    return node

def print_node(node):
    while node:
        print(node.value,end=" ")
        node = node.next
    print()

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
a.next = b
b.next = c
c.next = d
d.next = e

print_node(a)
del_mid_node(a)
print_node(a)
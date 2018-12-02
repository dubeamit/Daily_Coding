class Node:
    def __init__(self, value = None):
        self.value = value
        self.next_node = None

def remove_duplicate(node):
    dictionary = {}
    curr = node
    prev = Node()
    while curr:
        if curr.value in dictionary:
            if curr.next_node:
                prev.next_node = curr.next_node
                curr.next_node = None
            else:
                prev.next_node = None
            curr.next_node = None
            curr = prev
        else:
            dictionary[curr.value] = 1
            prev = curr
        curr = curr.next_node

def print_ll(node):
    while node:
        print(node.value)
        node = node.next_node

a = Node(1)
b = Node(2)
c = Node(5)
d = Node(2)
e = Node(5)
a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e

remove_duplicate(a)
print_ll(a)
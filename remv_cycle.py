class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

def detect_loop(node):
    slow = fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if slow == fast:
        slow = node
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None
    print_ll(node)

def print_ll(node):
    while node:
        print(node.data)
        node = node.next

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d
d.next = b # Loop formed

detect_loop(a)

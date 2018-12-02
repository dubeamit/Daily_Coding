class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
def reverse_ll(head):
    cur = head
    next = prev = None

    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next 
    display(prev)

def display(head):
    while head:
        print(head.data)
        head = head.next

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

reverse_ll(a)
# Detect cycle in Linked list
class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

def cycle_check(node):
    slow = node
    fast = node
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d
d.next = a # Cycle formed 

print(cycle_check(a))
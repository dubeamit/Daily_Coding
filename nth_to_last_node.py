# Return Nth to Last node in Linked List
# 1) have two pointer left_ptr = head and right_ptr = n
# 2) traverse one node at time till right_ptr is at last node and return left_ptr
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def nth_to_last_node(head,n):
    left_ptr = head
    right_ptr = head    
    for _ in range(n-1):
        if not right_ptr.next:
            return "N larger than Linked List"
        right_ptr = right_ptr.next

    while right_ptr.next:
        left_ptr = left_ptr.next
        right_ptr = right_ptr.next
    return left_ptr.data

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
a.next = b
b.next = c
c.next = d
d.next = e
n=2
print(n,"to last node is",nth_to_last_node(a,n)) # should print 4
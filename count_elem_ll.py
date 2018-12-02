# Write a function that counts the number of times a given int 
# occurs in a Linked List

class Node:
    def __init__(self, value = None):
        self.next = None
        self.value = value

def count_elem_ll(node, key):
    count = 0
    while node:
        if node.value == key:
            count += 1
        node = node.next
    return count

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(1)
a.next = b
b.next = c
c.next = d

print(count_elem_ll(a , 1))
print(count_elem_ll(a,0))
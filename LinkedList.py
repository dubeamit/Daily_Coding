# Linked List
class Node:
	def __init__(self, data = None):
		self.next = None
		self.data = data

class LinkedList:
	def __init__(self):
		self.head = Node() # wrap the Node class
	def push(self, data):
		new_node = Node(data)
		cur = self.head
		while cur.next:
			cur = cur.next
		cur.next = new_node
	def isEmpty(self):
		return self.head.next is None
	def pop(self):
		if self.isEmpty():
			return None
		cur = self.head
		while cur.next.next:
			cur = cur.next
		pop = cur.next.data
		cur.next = None
		return pop
	def display(self):
		elements = []
		cur = self.head
		while cur.next:
			cur = cur.next
			elements.append(cur.data)
		return elements

ll = LinkedList()
print('Is Empty', ll.isEmpty())
print('Pop', ll.pop())
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
print('Is Empty', ll.isEmpty())
print('Print', ll.display())
print('Pop', ll.pop())
print('Print', ll.display())
# Creating Stack
class Stack:
    def __init__(self):
        self.items = [] # Creating a list
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.items == []:
            return 'empty stack: underflow'
        return self.items.pop()
    def peek(self):
        if self.items == []:
            return 'Empty stack: underflow'
        return self.items[len(self.items)-1]
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

s = Stack()
print(s.pop())
s.push('#100 days of code')
s.push('Day 9 of code')
print(s.peek())
print(s.isEmpty())
print(s.size())
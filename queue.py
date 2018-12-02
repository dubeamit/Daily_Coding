# Queue implementation --> FIFO
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item): # insert to rear
        self.items.insert(0,item)
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty!!!!"
        return self.items.pop()
    def size(self):
        return len(self.items)

q = Queue()
print(q.dequeue())
print(q.isEmpty())
q.enqueue('Day 9 of Data Structures & Algorithms')
q.enqueue('implementation of queues is python')
print(q.size())
print('removing items from queue:',q.dequeue())
print(q.size())

class queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self,data):
        self.items.append(data)
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
    def show(self):
        print("Queue:", self.items)


Queue = queue()

Queue.enqueue(1)
Queue.show()  # Should show [1]
Queue.enqueue(2)
Queue.show()  # Should show [1, 2]
Queue.enqueue(3)
Queue.show()  # Should show [1, 2, 3]
Queue.enqueue(4)
Queue.show()  # Should show [1, 2, 3, 4]
Queue.enqueue(5)
Queue.show()  # Should show [1, 2, 3, 4, 5]

Queue.dequeue()
Queue.show()  # Should show [2, 3, 4, 5]



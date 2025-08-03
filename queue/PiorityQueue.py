class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.assign_value = {}
    
    def set_value(self,item,value):
        self.assign_value[item] = value
    def enqueue(self,item):
        self.queue.append(item)
        if len(self.queue) > 1:
            if item in self.assign_value:
                i = len(self.queue) - 1
                while(i > 0):
                    if self.assign_value[self.queue[i]] > self.assign_value[self.queue[i - 1]]:
                        # Swap the items
                        self.queue[i], self.queue[i - 1] = self.queue[i - 1], self.queue[i]

                    i -= 1
                    
            else:
                self.assign_value[item] = 0
    def dequeue(self):
        if not self.is_empty():
            self.queue.pop(0)
            return True
        else:
            return False
    def is_empty(self):
        return len(self.queue) == 0

    def show(self):
        print("Priority Queue:", self.queue)

queue = PriorityQueue()
queue.set_value("A", 4)
queue.set_value("B", 3)
queue.set_value("C", 2)
queue.set_value("D", 1)

queue.enqueue("A")
queue.show()  # Should show ["A"]
queue.enqueue("B")
queue.show()  # Should show ["B", "A"]
queue.enqueue("C")
queue.show()  # Should show ["C", "B", "A"]
queue.enqueue("D")
queue.show()  # Should show ["C", "B", "A", "D"]



queue.enqueue("A")
queue.show() 

queue.enqueue("B")
queue.show()  
queue.enqueue("B")
queue.show()  
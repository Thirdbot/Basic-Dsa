import sys
class maxheap:
    def __init__(self,length):
        self.length = length
        self.n = 0
        self.a = [0] * (length + 1)
        self.a[0] = sys.maxsize
        self.root = 1 #as an index
        
    def parent(self,i):
        return i//2

    def left(self,i):
        return 2*i
        
    def right(self,i):
        return 2*i+1
    
    def isLeaf(self,i):
        return i > (self.n // 2) and i <= self.n
    
    def swap(self,i,j):
        self.a[i],self.a[j] = self.a[j],self.a[i]
        
    def heapify(self,i):
        if not self.isLeaf(i):
            largest = i
            if self.left(i) <= self.n and self.a[i] < self.a[self.left(i)]:
                largest = self.left(i)
            if self.right(i) <= self.n and self.a[largest] < self.a[self.right(i)]:
                largest = self.right(i)
            if largest != i:
                self.swap(i,largest)
                self.heapify(largest)
    
    def insert(self,val):
        if self.n >= self.length:
            return
        self.n += 1
        self.a[self.n] = val
        i = self.n
        while self.a[i] > self.a[self.parent(i)]:
            self.swap(i,self.parent(i))
            i = self.parent(i)
    
    def findmax(self):
        if self.n == 0:
            return None
        max_val = self.a[self.root]
        self.a[self.root] = self.a[self.n]
        self.n -= 1
        self.heapify(self.root)
        return max_val
    
    def printheap(self):
        for i in range(1, (self.n // 2) + 1):
            print(f"PARENT: {self.a[i]}", end=" ")
            if self.left(i) <= self.n:
                print(f"LEFT: {self.a[self.left(i)]}", end=" ")
            if self.right(i) <= self.n:
                print(f"RIGHT: {self.a[self.right(i)]}", end=" ")
            print()

if __name__ == "__main__":
    print("The maxHeap is:")
    h = maxheap(15)
    vals = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    for val in vals:
        h.insert(val)

    h.printheap()
    print("The Max val is", h.findmax())
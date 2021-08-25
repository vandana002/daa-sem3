import sys
class max_heap:
def __init__(self, capacity):
self.capacity = capacity
self.size = 0

self.Heap = [0]*(self.capacity + 1)
self.Heap[0] = sys.maxsize
self.root = 1
def swapnodes(self, node1, node2):
self.Heap[node1], self.Heap[node2] = self.Heap[node2], self.Heap[node1]
def max_heapify(self, i):
if not (i >= (self.size//2) and i <= self.size):
if (self.Heap[i] < self.Heap[2 * i] or self.Heap[i] < self.Heap[(2 * i) + 1]):
if self.Heap[2 * i] > self.Heap[(2 * i) + 1]:
# Swap the node with the left child and call the max_heapify function on it
self.swapnodes(i, 2 * i)
self.max_heapify(2 * i)
else:
self.swapnodes(i, (2 * i) + 1)
self.max_heapify((2 * i) + 1)
def heappush(self, element):
if self.size >= self.capacity :
return
self.size+= 1
self.Heap[self.size] = element
current = self.size
while self.Heap[current] > self.Heap[current//2]:
self.swapnodes(current, current//2)
current = current//2
def heappop(self):
last = self.Heap[self.root]
self.Heap[self.root] = self.Heap[self.size]
self.size -= 1
self.max_heapify(self.root)
return last
def build_heap(self):
for i in range(self.size//2, 0, -1):
self.max_heapify(i)
def print_heap(self):
for i in range(1, (self.size//2)+1):
print("Parent Node is "+ str(self.Heap[i])+" Left Child is "+ str(self.Heap[2 * i]) +
" Right Child is "+ str(self.Heap[2 * i + 1]))
maxHeap = max_heap(10)
maxHeap.heappush(15)
maxHeap.heappush(7)

maxHeap.heappush(9)
maxHeap.heappush(4)
maxHeap.heappush(13)
maxHeap.print_heap()

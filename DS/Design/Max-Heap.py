class MaxHeap:
    def __init__(self):
        # Initialize with empty array
        self.heap = []

    def insert(self, val):
        # Insert at end
        self.heap.append(val)
        # Percolate up
        self.__percolateUp(len(self.heap)-1)

    def getMax(self):
        if self.heap:
            return self.heap[0]
        return None

    def removeMax(self):
        # Swap root with last leaf
        if len(self.heap) > 1:
            max = self.heap[0]
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            # Delete last node
            del self.heap[-1]
            # Heapify
            self.__maxHeapify(0)
            return max
        elif len(self.heap) == 1:
            max = self.heap[0]
            del self.heap[0]
            return max 

    def __percolateUp(self, index):
        parent = (index-1)//2
        # Base Case
        if index <= 0:
            return
        elif(self.heap[parent] < self.heap[index]):
            # Swap
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            # Recursively call _percolateUp on parent
            self.__percolateUp(parent)

    def __maxHeapify(self, index):
        left = (2*index) +  1
        right = (2*index) +  2
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.__maxHeapify(largest)
            
    def buildHeap(self, arr):
        self.heap = arr
        for i in range(len(arr)-1, -1, -1):
            self.__maxHeapify(i)


heap = MaxHeap()
heap.insert(12)
heap.insert(10)
heap.insert(-10)
heap.insert(100)

print(heap.getMax())
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def __str__(self):
        return str(self.heap)

heap = MaxHeap()
values = [5, 3, 8, 1, 2, 7, 6, 4]
for value in values:
    heap.insert(value)
print(heap)
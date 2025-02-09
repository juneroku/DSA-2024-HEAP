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

    def delete_max(self):
        if not self.heap:
            return None
        max_value = self.heap[0]
        last_element = self.heap.pop()
        if self.heap:
            self.heap[0] = last_element
            self._heapify_down(0)
        return max_value

    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def __str__(self):  # For easy printing of the heap
        return str(self.heap)


heap = MaxHeap()
values = [5, 3, 8, 1, 2, 7, 6, 4]
for value in values:
    heap.insert(value) # Now the insert method exists

print("Max Heap เริ่มต้น:", heap)
for i in range(3):
    deleted_value = heap.delete_max()
    print(f"ลบค่าสูงสุด {deleted_value}:", heap)
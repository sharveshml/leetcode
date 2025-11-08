class MinHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, value):
        self.heap.append(value)
        self._shift_up(len(self.heap)-1)
    
    def pop(self):
        if not self.heap:
            return None

        self._swap(0, len(self.heap)-1)
        val = self.heap.pop()
        self._shift_down(0)

        return val

    def _shift_up(self, i):
        parent = (i-1) // 2

        while i > 0 and self.heap[i] < self.heap[parent]:
            self._swap(i, parent)
            i = parent
            parent = (i-1) // 2
    
    def _shift_down(self, i):
        n = len(self.heap)

        while True:
            smallest = i
            left = i*2+1
            right = i*2+2

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break
            self._swap(smallest, i)
            i = smallest
    
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


# h = MinHeap()
# for x in [5, 1, 8, 3, 2]:
#     h.push(x)
# print(h.pop())  # 1
# print(h.pop())  # 2
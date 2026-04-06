class MinHeap:
    
    def __init__(self):
        self.heap = [0]
        
    # O(log(n))
    def push(self, val: int) -> None:
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    # O(log(n))
    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._bubble_down(1)
        return res
        
    # O(1)
    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1
        
    # O(n)
    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        for i in reversed(range(1, len(self.heap) // 2 + 1)):
            self._bubble_down(i)
    
    def _bubble_up(self, index: int) -> None:
        parent = index // 2
        while index > 1 and self.heap[parent] > self.heap[index]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = index // 2
    
    def _bubble_down(self, index: int) -> None:
        while index * 2 < len(self.heap):
            left_child = index * 2
            right_child = index * 2 + 1
            if right_child < len(self.heap) and self.heap[left_child] > self.heap[right_child] and self.heap[right_child] < self.heap[index]:
                self.heap[right_child], self.heap[index] = self.heap[index], self.heap[right_child]
                index = right_child
            elif self.heap[left_child] < self.heap[index]:
                self.heap[left_child], self.heap[index] = self.heap[index], self.heap[left_child]
                index = left_child
            else:
                break








        
        
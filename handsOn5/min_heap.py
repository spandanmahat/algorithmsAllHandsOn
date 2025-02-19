from typing import List, TypeVar, Generic

T = TypeVar('T')

class MinHeap(Generic[T]):
    def __init__(self, elements: List[T] = None):
        self.heap = elements or []
        if self.heap:
            self.build_min_heap()

    def _parent(self, i: int) -> int:
        return (i - 1) >> 1  #(i-1)/2 since array starts at index 0

    def _left_child(self, i: int) -> int:
        return (i << 1) + 1  #(i*2)+1

    def _right_child(self, i: int) -> int:
        return (i << 1) + 2  #(i*2)+2

    def heapify(self, i: int):
        smallest = i
        left = self._left_child(i)
        right = self._right_child(i)
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest!= i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def build_min_heap(self):
        for i in range((len(self.heap) - 1) >> 1, -1, -1):
            self.heapify(i)

    def pop(self) -> T:
        if not self.heap:
            raise IndexError("Heap is empty")
        root = self.heap[0]
        last_element = self.heap.pop()
        if self.heap:
            self.heap[0] = last_element
            self.heapify(0)
        return root

    def peek(self) -> T:
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]
    
    def __repr__(self):
        return str(self.heap)

def main():
    nums = [100, 19, 36, 17, 3, 25, 1]
    heap = MinHeap(nums)
    print("Built Heap: ", heap)
    print("Popped element: ", heap.pop())
    print("Heap after pop: ", heap)
    print("Peek element: ", heap.peek())

    print("\n\n\n")
    nums1 = [50.0, 22.1, 30.5, 5.9, 18.3, 10.2, 45.7]
    heap1 = MinHeap(nums1)
    print("Built Heap: ", heap1)
    print("Popped element: ", heap1.pop())
    print("Heap after pop: ", heap1)
    print("Peek element: ", heap1.peek())

if __name__ == "__main__":
    main()

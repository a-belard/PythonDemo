import sys

from scipydemo import scipydemo


class MinHeap:
    def __init__(self, heap_size):
        self.heapSize = heap_size
        self.minHeap = [0] * (heap_size + 1)
        self.realSize = 0

    def add_element(self, data):
        self.realSize += 1
        if self.realSize > self.heapSize:
            print("Heap overflow")
            self.realSize -= 1
            return

        self.minHeap[self.realSize] = data
        index = self.realSize
        parent = index // 2
        while self.minHeap[index] < self.minHeap[parent] and index > 1:
            self.minHeap[index], self.minHeap[parent] = self.minHeap[parent], self.minHeap[index]
            index = parent
            parent = index // 2

    def display(self):
        if self.realSize == 0:
            print("No elements yet")
        print(self.minHeap[1:])

    def peek(self):
        if self.realSize == 0:
            return "No elements yet"
        return self.minHeap[1]

    def pop(self):
        if self.realSize == 0:
            print("No elements")
            return sys.maxsize
        remove_element = self.minHeap[1]
        self.minHeap[1] = self.minHeap[self.realSize]
        index = 1
        self.realSize -= 1
        while index <= self.realSize // 2:
            left_child = index * 2
            right_child = (index * 2) + 1
            if self.minHeap[index] > self.minHeap[left_child] or self.minHeap[index] > self.minHeap[right_child]:
                if self.minHeap[right_child] > self.minHeap[left_child]:
                    self.minHeap[index], self.minHeap[left_child] = self.minHeap[left_child], self.minHeap[index]
                    index = left_child
                else:
                    self.minHeap[index], self.minHeap[right_child] = self.minHeap[right_child], self.minHeap[index]
                    index = right_child
            else:
                break
        return remove_element
    def __str__(self):
            return str(self.minHeap[1: self.realSize + 1])

minHeap = MinHeap(6)
minHeap.add_element(30)
minHeap.add_element(5)
minHeap.add_element(10)
minHeap.add_element(4)
minHeap.add_element(3)
print(minHeap)
minHeap.pop()
print(minHeap.peek())
print(minHeap)

scipydemo

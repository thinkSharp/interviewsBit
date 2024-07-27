import unittest
"""
Problem:
You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)] such that, for each index i (between 0 and n-1, inclusive), output[i] is equal to the product of the three largest elements out of arr[0..i] (or equal to -1 if i < 2, as arr[0..i] then includes fewer than three elements).
Note that the three largest elements used to form any product may have the same values as one another, but they must be at different indices in arr.

Solution Approach:
Example: [1,2,3,4,5]
specifically talking about 3 largest till ith from 0, if less then 2 then -1
answer is [-1,-1,6,24,60]

Sort the array
 - just to learn heap sort I am going to implement heap sort
loop through the array list to get 

time complexity : O(nlogn + n) => O (nlogn) is for heap sort (aka) priority sort
space complexity : O(n)
"""
class Heap:
    def __init__(self) -> None:
        self._heap = []
    
    def heapify(self, index):
        n = len(self._heap) 
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < n and self._heap[left] > self._heap[largest]:
            largest = left
        
        if right < n and self._heap[right] > self._heap[largest]:
            largest = right

        if largest != index:
            self._heap[largest], self._heap[index] = self._heap[index], self._heap[largest]
            self.heapify(largest)

    def insert(self, value):
        self._heap.append(value)
        index = len(self._heap) - 1
        

        while index != 0:
            parent = (index - 1) // 2
            if self._heap[index] > self._heap[parent]:
                self._heap[parent], self._heap[index] = self._heap[index], self._heap[parent]
                index = parent
            else:
                break
        
    def extract_max(self):
        if len(self._heap) == 0:
            return None
        
        if len(self._heap) == 1:
            return self._heap.pop()
        

        value = self._heap[0]
        self._heap[0] = self._heap.pop()
        self.heapify(0)

        return value
    
    def get_max_value(self):
        if len(self._heap) == 0:
            return None
        return self._heap[0]
    
    def size(self):
        return len(self._heap)
    
    def is_empty(self):
        return len(self._heap) == 0
    
    def display(self):
        return print(self._heap)
    
    def get_heapify_array(self):
        arr = self._heap[:]
        return arr
    
def heap_sort(arr):
    heap = Heap()

    for item in arr:
        heap.insert(item)
    
    return heap

def findMaxProduct(arr):
    n = len(arr)
    if n == 0:
        return []
    if n == 1:
        return [-1]
    if n == 2:
        return [-1,-1]
    
    heap = heap_sort(arr)
    first = heap.extract_max()
    second = heap.extract_max()

    result = []
    for _ in range(n-1, 1, -1):
        third = heap.extract_max()
        result.append(first * second * third)
        first = second
        second = third

    result.append(-1)
    result.append(-1)

    return result[::-1]

class TestSolution(unittest.TestCase):
    def test_given_cases(self):
        self.assertEqual(findMaxProduct([2,1,2,1,2]), [-1,-1,2,4,8])
        self.assertEqual(findMaxProduct([1,2,3,4,5]), [-1,-1,6,24,60])
        self.assertEqual(findMaxProduct([2,4,7,1,5,3]),[-1,-1,56,56,140,140])

if __name__ == '__main__':
    unittest.main()


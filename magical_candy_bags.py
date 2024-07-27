import unittest
"""
Problem:
You have N bags of candy. The ith bag contains arr[i] pieces of candy, and each of the bags is magical!
It takes you 1 minute to eat all of the pieces of candy in a bag (irrespective of how many pieces of candy are inside), and as soon as you finish, the bag mysteriously refills. If there were x pieces of candy in the bag at the beginning of the minute, then after you've finished you'll find that floor(x/2) pieces are now inside.
You have k minutes to eat as much candy as possible. How many pieces of candy can you eat?

Understand the Problem:
- N magic bags
- depending on the position of the bag in the array, it contains that number of candy
- candies in 1 bag per minutes 
- bag auto refill x// 2 candies
- given number of minutes how many candies did you eat?

Solution approach:
- always pick a bag which has max candies
- max_heap would be great for this solution
- in python there is a heapq that I can use to implmement
- or if you want me to implement heap, I can do that as well
- for practice I will

Heap implementation:
MaxHeap:
  - heapify 
  - insert
  - extract_max

maxCandies(arr, k):
 - build heap
 - result
 - loop thrugh no. of minutes
    - result += extract_max
    - insert(x//2)
- return result

Complexity
- Time O(n logn + k) where n is the length of arr and k is minutes
- Space O(n) where n is the length of the arr
"""

class MaxHeap:
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
        index = len(self._heap) -1

        while index != 0:
            parent = (index -1) // 2
            if self._heap[parent] < self._heap[index]:
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
    
    def to_list(self):
        return self._heap[:]
    
def maxCandies(arr,k):
    n = len(arr)
    if n == 0:
        return 0
    
    heap = MaxHeap()
    for i in range(n):
        heap.insert(arr[i])

    print(heap.to_list())
    result = 0

    for _ in range(k):
        max_candy = heap.extract_max()
        result += max_candy
        heap.insert(max_candy // 2)
    
    return result

class TestSolution(unittest.TestCase):
    def test_given_cases(self):
        self.assertEqual(maxCandies([2,1,7,4,2], 3), 14)
        self.assertEqual(maxCandies([19,78,76,72,48,8,24,74,29], 3), 228)

if __name__ == '__main__':
    unittest.main()

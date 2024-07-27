import unittest
import heapq

"""
Problem:
You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)] such that, for each index i (between 0 and n-1, inclusive), output[i] is equal to the median of the elements arr[0..i] (rounded down to the nearest integer).
The median of a list of integers is defined as follows. If the integers were to be sorted, then:
If there are an odd number of integers, then the median is equal to the middle integer in the sorted order.
Otherwise, if there are an even number of integers, then the median is equal to the average of the two middle-most integers in the sorted order.

Understand the probem:
we will have array of integer
loop through the array
   - sort
   - calculate the median
        - odd lenght then middle
        - even then two middle plus // 2

solution approach:
- sort till i in the loop
    - heap sort is the great candidate 
    - will utilize built in heapq
        have 2 heap
        max_heap stores negative values 
        min_head stores values as it is
- calculate the median
- add in the result 

Time complexity => O(nlogn) where n is the length of array and log n is the time it takes to insert or delete from heap
Space Complexity => O(n) for 2 heaps as they will share the elements + O(n) for output so O(n)
"""

def findMedian(arr):
    n = len(arr)
    if n == 0:
        return []
    
    min_heap = []
    max_heap = []
    result = []

    for num in arr:
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        if len(max_heap) > len(min_heap):
            median = -max_heap[0]
        else:
            median = (-max_heap[0] + min_heap[0]) // 2
        
        result.append(median)
    
    return result

class TestSolution(unittest.TestCase):
    def test_given_cases(self):
        self.assertEqual(findMedian([5,15,1,3]),[5,10,5,4])
        self.assertEqual(findMedian([1,2]), [1,1])
        self.assertEqual(findMedian([2,4,7,1,5,3]),[2,3,4,3,4,3])


if __name__ == '__main__':
    unittest.main()


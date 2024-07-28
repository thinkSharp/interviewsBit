import unittest
from collections import deque
"""
Problem:
There are n guests attending a dinner party, numbered from 1 to n. The ith guest has a height of arr[i-1] inches.
The guests will sit down at a circular table which has n seats, numbered from 1 to n in clockwise order around the table. As the host, you will choose how to arrange the guests, one per seat. Note that there are n! possible permutations of seat assignments.
Once the guests have sat down, the awkwardness between a pair of guests sitting in adjacent seats is defined as the absolute difference between their two heights. Note that, because the table is circular, seats 1 and n are considered to be adjacent to one another, and that there are therefore n pairs of adjacent guests.
The overall awkwardness of the seating arrangement is then defined as the maximum awkwardness of any pair of adjacent guests. Determine the minimum possible overall awkwardness of any seating arrangement.

Problem Understanding:
finding smallest overall awkwardness from the array of people sitting in round table. 
which mean last table and first table are next to each other

Example:
[5,10,6,8] to minimize the maximum arkwardness, I would sort the array.
[5,6,8,10] => take the max and put it in dqueue
[10] => then pop one element at a time from array, insert them alternative from left to right
[8,10] => [8,10,6] => [5,8,10,6] => maximum arkwardness is 4

Pseudo code:

max_awkwardness
sort the array 
create dqueue
loop the sorted array
    pop one element at a time and alternatively 
    append_left or
    append
    calculate the awkwardness
    store the max awkwardness

return max_awkwardness

Time complexity: sorting an array O(nlogn), re arrange in Q O(n) => O(nlogn)
Space Complexity: O(n) for sorting, O(n) for deque
"""
def minOverallAwkwardness(arr):
    n = len(arr)
    if n <= 1:
        return 0
    
    queue = deque()
    sorted_arr = sorted(arr)
    queue.append(sorted_arr[-1])
    for i in range(n-2, -1,-1):
        if i % 2 == 0:
            queue.append(sorted_arr[i])
        else:
            queue.appendleft(sorted_arr[i])
    
    max_awkwardness = 0
    for j in range(1, n):
        max_awkwardness = max(max_awkwardness, abs(queue[j] - queue[j-1]))

    max_awkwardness = max(max_awkwardness, abs(queue[-1] - queue[0]))

    return max_awkwardness

class TestSolution(unittest.TestCase):
    def test_given_cases(self):
        self.assertEqual(minOverallAwkwardness([5,10,6,8]), 4)
        self.assertEqual(minOverallAwkwardness([1,2,5,3,7]), 4)
    
    def test_edge_cases(self):
        self.assertEqual(minOverallAwkwardness([1]), 0)
        self.assertEqual(minOverallAwkwardness([1,1]), 0)

    def test_long_array_cases(self):
        self.assertEqual(minOverallAwkwardness([2,10,20,5,7,15,8,9]), 10)


if __name__ == '__main__':
    unittest.main()

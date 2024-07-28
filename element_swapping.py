import unittest
from collections import defaultdict
"""
Problem:
Given a sequence of n integers arr, determine the lexicographically smallest sequence which may be obtained from it after performing at most k element swaps, each involving a pair of consecutive elements in the sequence.
Note: A list x is lexicographically smaller than a different equal-length list y if and only if, for the earliest index at which the two lists differ, x's element at that index is smaller than y's element at that index.

Understanding the Problem:
finding the lexicographically smallest sequence by swapping k time. 
- each swap is involving swapping pair of consecutive element

Example:
[5,3,1] k = 2
[5,3,1] => [5,1,3] => [1,5,3]

[8,9,11,2,1], k = 3
[8,9,11,2,1] => [8,9,2,11,1] => [8,2,9,11,1] => [2,8,9,11,1]

[9,8,7,2,1], k = 5
[9,8,7,2,1], => [9,8,7,1,2] => [9,8,1,7,2] => [9,1,8,7,2] => [1,9,8,7,2] => [1,8,9,7,2] 

find the lowerst number that can be moved which is less then or equal to k
if k remains, repeat the same process

pseudo code:
    for i in range(n)
        pos = i
        from j in range(i+1, min(i+k+1, n)):
            if arr[j] < arr[pos]
                pos = j

        swap_needed = pos - i

        if swap_needed >= k:
            while pos > i:
                arr[pos], arr[pos-1] = arr[pos-1], arr[pos]
                pos -= 1
        k -= swap_needed


time complexity: o(n2) where n is the length of array
space complexity: O(1)
"""

def findMinArray(arr, k):
    n = len(arr)
    for i in range(n):
        pos = i
        for j in range(i+1, min(i+k+1, n)):
            if arr[j] < arr[pos]:
                pos = j
        
        swap_needed = pos - i
        
        if swap_needed <= k:
            while pos > i:
                arr[pos], arr[pos-1] = arr[pos-1], arr[pos]
                pos -=1
        
        k -= swap_needed
    return arr



class TestSolution(unittest.TestCase):
    def test_given_cases(self):
        self.assertEqual(findMinArray([1,9,8,7,2], 1), [1,8,9,7,2])
        self.assertEqual(findMinArray([1,8,9,7,2], 1), [1,8,7,9,2])
        self.assertEqual(findMinArray([5,3,1], 2), [1,5,3])
        self.assertEqual(findMinArray([8,9,11,2,1], 3), [2,8,9,11,1])
        


if __name__ == '__main__':
    unittest.main()

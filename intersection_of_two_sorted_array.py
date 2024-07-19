import unittest
from collections import Counter

"""
Problem Statement:
Find the intersection of two sorted arrays OR in other words, given 2 sorted arrays, find all the elements which occur in both arrays.

NOTE: For the purpose of this problem ( as also conveyed by the sample case ), assume that elements that appear more than once in both arrays should be included multiple times in the final output.

Solution outline:

build two counters and count all the elements of the arrays
loop the smaller array to check the interset elements in bigger error
  - Since the count will tell us how many same element in smaller array, the loop will take the none zero min value
"""

class Solution:
    def intersect(self, A, B):
        counter_a = Counter(A)
        counter_b = Counter(B)
        
        interset_array = []

        for key in counter_a:
            if key in counter_b:
                interset_array.extend([key] * min(counter_a[key], counter_b[key]))
               

        return interset_array
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_simple_test_cases(self):
        self.assertEqual(self.sol.intersect([1,2,3,3,4,5,6],[3,3,5]),[3,3,5])
        self.assertEqual(self.sol.intersect([],[1,2,3]),[])
        self.assertEqual(self.sol.intersect([1,1,1,1,3,3,3,3,3,5,5,5,5,5,5],[1,5,5,5,5]),[1,5,5,5,5])


if __name__ == "__main__":
    unittest.main()
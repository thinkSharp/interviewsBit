import unittest
from collections import defaultdict

class Solution:
    """
    Given an array of size N, find the majority element. The majority element is the element that appears more than floor(N/2) times.
    You may assume that the array is non-empty and the majority element always exist in the array.
    """
    def majorityElement(self,A):
        mid = len(A) // 2
        counter = defaultdict(int)
        for item in A:
            counter[item] +=1
        
        for key, value in counter.items():
            if value > mid:
                return key
            
        return  -1
    

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_test_cases(self):
        self.assertEqual(self.sol.majorityElement([2,1,2]), 2)
        self.assertEqual(self.sol.majorityElement([2,2,2,2,4,4,4,4,3,2,3,6,7,6,2,2,2,2,2]), 2)


if __name__ == '__main__':
    unittest.main()

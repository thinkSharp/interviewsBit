import unittest
"""
problem statement:

Given an sorted array A of size N. Find number of elements which are less than or equal to B.

NOTE: Expected Time Complexity O(log N)

Solution Outline:

using binary search find the position of last number which is less then equal to B
once we find that, grab all the number till from begining till that number
"""

class Solution:

    def binary_search(self, A, B, left, right):
            while left <= right:
                mid = left + (right - left) // 2
                if A[mid] <= B:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
    
    def binary_search_bad(self, A, B, left, right):
        if left >= right:
            return -1
        
        mid = left + (right - left ) // 2

        if mid + 1 == right and A[right] <= B:
            return right           

        if A[mid] <= B and A[mid+1] > B:
            return mid
        elif A[mid]<=B and A[mid+1] <= B:
            left = mid
        else:
            right = mid
        return self.binary_search(A,B,left,right)
        


    def solve(self, A, B):
        
        pos = self.binary_search(A,B,0, len(A)-1)
        return pos + 1
    
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_simple_cases(self):
        
        self.assertEqual(self.sol.solve([1,3,4,4,6], 4), 4)
        self.assertEqual(self.sol.solve([1,3,4,4,6], 0), 0)
        self.assertEqual(self.sol.solve([1,3,4,4,6], 1), 1)
        self.assertEqual(self.sol.solve([1,3,4,4,6], 8), 5)
        self.assertEqual(self.sol.solve([1,2,5,5], 3), 2)


if __name__ == '__main__':
    unittest.main()
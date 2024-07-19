import unittest

class Solution:
    """
    Given a bitonic sequence A of N distinct elements, write a program to find a given element B in the bitonic sequence in O(logN) time.

NOTE:

A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.
    """
    def solve(self, A, B):
        if not A:
            return -1
        
        return self.binary_search(A,B, 0, len(A) -1)

    def binary_search(self, A, B, left, right):
        if left > right:
            return -1
        
        mid = left + (right - left) // 2

        if A[mid] == B:
            return mid
   
        left_val = self.binary_search(A, B, left, mid -1)

        right_val = self.binary_search(A,B, mid +1, right)

        return max(left_val, right_val)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_test_cases(self):
        self.assertEqual(self.sol.solve([2],2),0)
        self.assertEqual(self.sol.solve([10,29,39,8,7,6,5,4,3,2,1], 2), 9)
        self.assertEqual(self.sol.solve([3,9,10,20,17,5,1], 20), 3)
        self.assertEqual(self.sol.solve([5,6,7,8,9,10,3,2,1], 30), -1)
       

if __name__ == "__main__":
    unittest.main()
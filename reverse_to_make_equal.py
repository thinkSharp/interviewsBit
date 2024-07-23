import unittest

"""
Problem Statement:
Given two arrays A and B of length N, determine if there is a way to make A equal to B by reversing any subarrays from array B any number of times.

Solution Steps:
Find the left most diff.
find the right most diff

Once find the sub array left and right index, swap the values
"""
class Solution:
    def solve(self, array_a, array_b):
        left, right = 0, len(array_a) -1
        while left < len(array_a) and array_a[left] == array_b[left]:
            left += 1
        
        while right >= 0 and array_a[right] == array_b[right]:
            right -= 1
        
        # swap
        while left < right:
            temp = array_b[left]
            array_b[left] = array_b[right]
            array_b[right] = temp
            left += 1
            right -= 1
        
        return array_a == array_b
    

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_test_cases(self):
        self.assertEqual(self.sol.solve([1,2,3,4], [1,4,3,2]), True)
        self.assertEqual(self.sol.solve([1,2,3,4], [1,2,3,5]), False)
        self.assertEqual(self.sol.solve([1,2,3,4], [4,3,2,1]), True)

if __name__ == "__main__":
    unittest.main()

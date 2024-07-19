import unittest
"""
Problem Description:
Given a string, determine if it is a palindrome. While checking for a palindrome, you have to ignore spaces, case, and all special characters; i.e. consider only alphanumeric characters.

Check the sample test case for reference.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Solution Outline:

first remove spaces, special character and lower all character
second loop len // 2 and compare first and last element 
"""

class Solution:
    def extract_alphanumeric(self, s):
        return ''.join([char.lower() for char in s if char.isalnum()])
    
    def isPalindrome(self, A):
        strip_A = self.extract_alphanumeric(A)
        mid = len(strip_A) // 2
        forward = 0
        backward = -1
        while mid > 0:
            if strip_A[forward] != strip_A[backward]:
                return 0
            forward += 1
            backward -= 1
            mid -= 1

        return 1
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_simple_cases(self):
        self.assertEqual(self.sol.isPalindrome('A man, a plan, a canal: Panama'), 1)
        self.assertEqual(self.sol.isPalindrome('race a car'), 0)


if __name__ == '__main__':
    unittest.main()
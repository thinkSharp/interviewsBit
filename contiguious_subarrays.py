import unittest
"""
Problem: You are given an array arr of N integers. For each index i, you are required to determine the number of contiguous subarrays that fulfill the following conditions:
The value at index i must be the maximum element in the contiguous subarrays, and
These contiguous subarrays must either start from or end on index i.

Solution Approach:
brute force approach:
left count 
    stack to go until and count
right count
    same thing on the right count
then add them together

[0, 1, 2, 3, 4, 5, 6, 7, 8]

[3, 4, 5, 1, 2, 3, 7, 6, 9]

[1, 2, 3, 1, 2, 3, 7, 1, 9]

[1, 1, 4, 1, 1, 1, 2, 1, 1]
"""
class Solution:
    def count_subarrays(self, arr):
        n = len(arr)
        left_connt = [0] * n
        right_count = [0] * n

        left_stack = []
        for i in range(n):
            while left_stack and arr[left_stack[-1]] < arr[i]:
                left_stack.pop()
            if left_stack:
                left_connt[i] = i - left_stack[-1]
            else:
                left_connt[i] = i + 1
            left_stack.append(i)
        
        right_stack = []
        for i in range(n-1, -1, -1):
            while right_stack and arr[right_stack[-1]] < arr[i]:
                right_stack.pop()
            
            if right_stack:
                right_count[i] = right_stack[-1] - i
            else:
                right_count[i] = n - i
            right_stack.append(i)

        result = [left_connt[i] + right_count[i] - 1 for i in range(n)]

        return result
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test_given_test_cases(self):
        self.assertEqual(self.sol.count_subarrays([3,4,1,6,2]), [1,3,1,5,1])

    def test_difficult_test_cases(self):

        self.assertEqual(self.sol.count_subarrays( [3, 4, 5, 1, 2, 3, 7, 6, 9]), [1, 2, 6, 1, 2, 3, 8, 1, 9])


if __name__ == '__main__':
    unittest.main()



import unittest
"""
Problem Statement:

Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

More formally,

    G[i] for an element A[i] = an element A[j] such that 
    j is maximum possible AND 
    j < i AND
    A[j] < A[i]
Elements for which no smaller element exist, consider next smaller element as -1.

Solution outline:

- initialize output array with -1
- loop through A
  - internal loop backward till 0 to find the nearest small value (if found set the value and break)
  - return
"""

class Solution:
    def prevSmaller(self, A):
        stack = []
        result = []

        for num in A:
            while stack and stack[-1] >= num:
                stack.pop()
            if stack:
                result.append(stack[-1])
            else:
                result.append(-1)
            stack.append(num)
        return result
    
    def prevSmaller_not_(self, A):
        if not A:
            return []
        
        return_list = [-1] * len(A)

        for i in range(len(A)):
            for j in range(i-1,-1, -1):
                if A[j] < A[i]:
                    return_list[i] = A[j]
                    break
        
        return return_list

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.prevSmaller([4,5,2,10,8]), [-1,4,-1,2,2])
        self.assertEqual(self.sol.prevSmaller([3,2,1]), [-1,-1,-1])
        self.assertEqual(self.sol.prevSmaller([3,2,1,10]), [-1,-1,-1, 1])
        self.assertEqual(self.sol.prevSmaller( [ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]),[-1,34,-1,27,-1,5,28,5,20])


if __name__ == '__main__':
    unittest.main()
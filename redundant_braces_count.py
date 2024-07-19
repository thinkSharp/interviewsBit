import unittest
from collections import deque
class Solution:
    def reverse_pop_until_key(self, stack, key):
        d = deque(stack)
        last_pop = ''
        while d:
            pop_element = d.pop()
            if pop_element == key :
                return list(d),0
            elif pop_element == '(' and last_pop == ')':
                return list(d),1
            last_pop = pop_element
            
        return list(d),0
    
    def braces(self, A):
        stack = []
        if not A:
            return 0
        for i in range(0, len(A)):            
            if A[i] in '()+-*/':
                stack.append(A[i])
                if A[i] == ')' and stack[-2] == '(':
                    return 1
                elif A[i] == ')':
                    stack, ret_val = self.reverse_pop_until_key(stack, '(')
                    if ret_val == 1:
                        return 1
        return 0




class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    def test_multiple_scenarios(self):
        self.assertEqual(self.sol.braces('((a+b))'), 1)
        self.assertEqual(self.sol.braces('(a +(a+b))'), 0)
        self.assertEqual(self.sol.braces('((a*b)+(c+d))'),0)
        self.assertEqual(self.sol.braces('(a*b)+(b*(d+(a)))'),1)

if __name__ == '__main__':
    unittest.main()
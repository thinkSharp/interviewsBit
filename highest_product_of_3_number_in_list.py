import unittest
class Solution:
	# @param A : list of integers
	# @return an integer
    def maxp3(self, A):
        A.sort(reverse=True)
        
        p1 = A[0] * A[1] * A[2]
        p2 = A[0] * A[-1] * A[-2]
        
        return max(p1, p2)
    

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test_given_scenarios(self):
        self.assertEqual(self.sol.maxp3([1,2,3,4]), 24)
        self.assertEqual(self.sol.maxp3([0,-1,3,100,70,50]),350000)
        self.assertEqual(self.sol.maxp3([0,-1,3,100,-70,-50]), 350000)


if __name__ == "__main__":
    unittest.main()
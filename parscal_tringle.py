import unittest
from collections import defaultdict
class Solution:
    def getRow(self, A):
        return self.get_parscal_row_space_efficient(A)

    def get_parscal_row_space_efficient(self, A):
        row = [1] * (A+1)
        for i in range(1, A):
            for j in range(i, 0, -1):
                row[j] += row[j-1]
        return row

    def build_parscal_tringle(self, A):
        parscal_dict = defaultdict(list)
        if A == 1:
            return [1]
        if A == 2:
            return [1,1]
        
        parscal_dict[0].append(1)
        parscal_dict[1] = [1,1]

        for i in range(2, A+1):
            parscal_dict[i].append(1)
            len_p = len(parscal_dict[i-1])
            prev_p = parscal_dict[i-1]
            for j in range(1,len_p):
                parscal_dict[i].append(prev_p[j-1]+ prev_p[j])
            parscal_dict[i].append(1)
        
        return parscal_dict[A]
    

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_simple_test_cases(self):
        self.assertEqual(self.sol.getRow(3), [1,3,3,1])
        self.assertEqual(self.sol.getRow(5), [1,5,10,10,5,1])

if __name__ == "__main__":
    unittest.main()





        
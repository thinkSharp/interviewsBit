import unittest
class Solution:
    # @param A : list of integers
    # @return an integer
    """
    Given a sorted array A consisting of duplicate elements.

    Your task is to remove all the duplicates and return the length of the sorted array of distinct elements consisting of all distinct elements present in A.

    Note: You need to update the elements of array A by removing all the duplicates
    """
    def removeDuplicates(self, A):
        if not A:
            return 0
        
        index = 1

        for i in range(1, len(A)):
            if A[i] != A[i-1]:
                A[index] = A[i]
                index += 1
        
        A[:] = A[:index]

        return index

    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_no_dup_count(self):
        A = [1,2,3,4]
        self.assertEqual(self.solution.removeDuplicates(A), 4)

    def test_one_dup_count(self):
        A = [1,2,2,3,4]
        self.assertEqual(self.solution.removeDuplicates(A), 4)
        self.assertEqual(A, [1,2,3,4])
    
    def test_multi_dup_count(self):
        self.assertEqual(self.solution.removeDuplicates([1,1,1,1,2,2,2,2,3,3,3,4,4]), 4)

if __name__ == "__main__":
    unittest.main()
    
    

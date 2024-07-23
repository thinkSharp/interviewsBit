import unittest

"""
There are n students, numbered from 1 to n, each with their own yearbook. They would like to pass their yearbooks around and get them signed by other students.
You're given a list of n integers arr[1..n], which is guaranteed to be a permutation of 1..n (in other words, it includes the integers from 1 to n exactly once each, in some order). The meaning of this list is described below.
Initially, each student is holding their own yearbook. The students will then repeat the following two steps each minute: Each student i will first sign the yearbook that they're currently holding (which may either belong to themselves or to another student), and then they'll pass it to student arr[i-1]. It's possible that arr[i-1] = i for any given i, in which case student i will pass their yearbook back to themselves. Once a student has received their own yearbook back, they will hold on to it and no longer participate in the passing process.
It's guaranteed that, for any possible valid input, each student will eventually receive their own yearbook back and will never end up holding more than one yearbook at a time.
You must compute a list of n integers output, whose element at i-1 is equal to the number of signatures that will be present in student i's yearbook once they receive it back.


Solution Outline:
signature count, result array initialize to 1
book in hand array initialize to own book denote with index of the student
incoming array contains who to pass

while all_done:
    all_done = false
    for i in range(len(array)):
        if book in hand != my own book:
            increment the signature of the index
            move book to [incoming array index]
            all_done = True

"""

class Solution:
    def solve(self, n, arr):
        signature = [1] * n
        books_in_hand = [0] * n
        for i in range(n):
            books_in_hand[arr[i]-1] = i

        pass_book = books_in_hand[:]
        all_done = False
        while not all_done:
            all_done = True
            for i in range(n):
                if books_in_hand[i] != i:
                    signature[books_in_hand[i]] += 1
                    pass_book[arr[i]-1] = books_in_hand[i]
                    all_done = False
            books_in_hand = pass_book[:]
        return signature



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_difficult_cases(self):
        self.assertEqual(self.sol.solve(5, [4,3,5,1,2]), [2,3,3,2,3])
        """
        arr = [3,2,4,0,1]
        signature = [2,3,2,2,3]
        books_in_hand = [0,2,4,3,1]
        pass_book = [0,1,2,3,4]
        """
    def test_given_test_cases(self):
        self.assertEqual(self.sol.solve(2, [2,1]), [2,2])
        self.assertEqual(self.sol.solve(2, [1,2]), [1,1])
if __name__ == "__main__":
    unittest.main()



import unittest
class Solution:
	# @param A : list of strings
	# @return a strings
    def longestCommonPrefix(self, A):
        if not A:
            return ''
        if len(A) == 1:
            return A[0]
        
        min_length = min(len(s) for s in A)
        prefix = ''
        current_val = ''
        for i in range(0, min_length):
            current_val = ''
            print(f'prefix : {prefix}, current_val: {current_val}, i : {i}, min_length: {min_length}')
            for a in A:
                print(f'current_val : {current_val}, a[i]: {a[i]}')
                if current_val == '' or current_val == a[i]:
                    current_val = a[i]
                else:
                    current_val = ''
                    break
            prefix += current_val
        return prefix

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_return_no_prefix(self):
        self.assertEqual(self.solution.longestCommonPrefix([]), '')

    def test_return_first_string_as_prefix(self):
        self.assertEqual(self.solution.longestCommonPrefix(['abcd']), 'abcd')

    def test_return_2_words_as_prefix(self):
        self.assertEqual(self.solution.longestCommonPrefix(['abcd', 'ab']), 'ab')

    def test_return_3_words_as_prefix(self):
        self.assertEqual(self.solution.longestCommonPrefix(["abcdefgh", "aefghijk", "abcefgh"]), 'a')
if __name__ == '__main__':
    unittest.main()


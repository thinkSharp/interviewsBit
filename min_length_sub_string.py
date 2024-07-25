import unittest
from collections import defaultdict, Counter
"""
problem: 
You are given two strings s and t. You can select any substring of string s and rearrange the characters of the selected substring. Determine the minimum length of the substring of s such that string t is a substring of the selected substring.

solution steps:
if s = 'dcbefebce'
and t = 'dfbe'


"""
def min_length_substring(s,t):
    char_index_map = defaultdict(list) 
    min_index, max_index = len(s), 0
    t_char_count = Counter(t)
    s_char_count = Counter(s)

    for index, ch in enumerate(s):
        char_index_map[ch].append(index)
    
    for ch in t:
        indexes = char_index_map[ch]
        if not indexes or t_char_count[ch] > s_char_count[ch]:
            return -1
        
        ch_index = min(indexes)
        min_index = min(min_index, ch_index)
        max_index = max(max_index, ch_index)

        if t_char_count[ch] > 1:
            ch_index = max(indexes)
            max_index = max(max_index, ch_index)
    
    return max_index - min_index + 1

class TestSolution(unittest.TestCase):
    def test_dup_sub_string_cases(self):
        self.assertEqual(min_length_substring('bdcbfbce', 'bbbc'), 6)
        self.assertEqual(min_length_substring('bdcbfbce', 'bbb'), 6)
    
    def test_given_cases(self):
        self.assertEqual(min_length_substring('dcbefebce', 'fd'), 5)

    def test_edge_cases(self):
        self.assertEqual(min_length_substring('dcbfbce', 'dcbe'), 7)
        self.assertEqual(min_length_substring('dcbefebce', 'jb'), -1)

if __name__ == '__main__':
    unittest.main()
        


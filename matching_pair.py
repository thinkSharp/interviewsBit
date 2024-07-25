import unittest
from collections import defaultdict
"""
Problem:
Given two strings s and t of length N, find the maximum number of possible matching pairs in strings s and t after swapping exactly two characters within s.
A swap is switching s[i] and s[j], where s[i] and s[j] denotes the character that is present at the ith and jth index of s, respectively. The matching pairs of the two strings are defined as the number of indices for which s[i] and t[i] are equal.
Note: This means you must swap two characters at different indices.

Solution Outline:
Ex: 
s = 'acdf'
t = 'ddae'

map {d: [0,1], a:[2], e:[3]}

loop: i = 0, s[i] = a, lookup 2
      j = 2  s[j] = d, lookup d in the map find list [0,1]

        s[i] = e, lookup 3
        j= 3, s[j] = f lookup 

"""

def matching_pairs(s,t):
    s1, t1 = [], []
    match_count = 0
    for cs, ct in zip(s,t):
        if cs == ct:
            match_count += 1
        else:
            s1.append(cs)
            t1.append(ct)
    t_lookup = defaultdict(list)
    
    for i, val in enumerate(t1):
        t_lookup[val].append(i)
    
    can_swap = False; increment = 0
    for i in range(len(s1)):
        indexes = t_lookup[s1[i]]
        for j in indexes:
            swap_indexes = t_lookup[s1[j]]
            if i in swap_indexes:
                increment = 2
                can_swap = True 
                break
        if can_swap:
            break
        elif len(indexes) > 0:
            increment = 1
            can_swap = True
         
    
    return match_count+increment if can_swap else max(match_count-2, 0)


class TestSolution(unittest.TestCase):
    def test_given_cases(self):
        self.assertEqual(matching_pairs('abcd', 'adcb'), 4)
        self.assertEqual(matching_pairs('mno', 'mno'),1)
        self.assertEqual(matching_pairs('mo', 'mo'),0)
        self.assertEqual(matching_pairs('lmnopqrst', 'lmnopqrst'),7)
        self.assertEqual(matching_pairs('ob', 'mo'),1)


if __name__ == '__main__':
    unittest.main()




    

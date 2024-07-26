import unittest
from collections import Counter
from math import comb

"""
Problem:
Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.
If an integer appears in the list multiple times, each copy is considered to be different; that is, two pairs are considered different if one pair includes at least one array index which the other doesn't, even if they include the same values.

Solution Apporach:
array [1,2,3,4,5,6,6,5,4]
k = 10
pair_count = 0
counter
loop through the counter 
 r = k - c
 look up r in the counter
  c 2 and r count = 3 then I will add 6 in the pair_count

"""
def numberOfWays(arr, k):
    count = Counter(arr)
    pair_count = 0
    visited = []
    for key, value in count.items():
        remainder = k - key
        if key in visited:
            continue

        if remainder == key:
            if value < 2:
                continue
            pair_count += comb(value,2)
        else:
            pair_count += value * count[remainder]
            visited.append(remainder)

    return pair_count

class TestSolution(unittest.TestCase):
    def test_given_cases(self):
        self.assertEqual(numberOfWays([1,2,3,4,3], 6), 2)
        self.assertEqual(numberOfWays([1,5,3,3,3], 6), 4) 
           

if __name__ == '__main__':
    unittest.main()
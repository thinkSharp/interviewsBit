import unittest
"""
question:
Given a list of N triangles with integer side lengths, determine how many different 
triangles there are. Two triangles are considered to be the same if they can both be placed on 
the plane such that their vertices occupy exactly the same three points.
answer approach:
given array of array with 3 sides, find the different tringles and return the count

example: [[2,2,3],[3,2,2],[2,5,6]] output = 2
My approach: sort the triangle arrays, and convert the list into set and return the len
"""

def countDistinctTriangles(arr):
    sorted_set = set()
    for a in arr:
        sorted_set.add(tuple(sorted(a)))
    
    return len(sorted_set)

class TestSolution(unittest.TestCase):
    def test_given_cases(self):
        self.assertEqual(countDistinctTriangles([[2,2,3],[3,2,2],[2,5,6]]), 2)
        self.assertEqual(countDistinctTriangles([[8, 4, 6], [100, 101, 102], [84, 93, 173]]), 3)
        self.assertEqual(countDistinctTriangles([[5, 8, 9], [5, 9, 8], [9, 5, 8], [9, 8, 5], [8, 9, 5], [8, 5, 9]]), 1)

if __name__ == '__main__':
    unittest.main()


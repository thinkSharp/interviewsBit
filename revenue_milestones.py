import unittest
"""
Problem statement:
We keep track of the revenue Facebook makes every day, and we want to know on what days Facebook hits certain revenue milestones. Given an array of the revenue on each day, and an array of milestones Facebook wants to reach, return an array containing the days on which Facebook reached every milestone.

Solutioon approach:
add the revenue and store in same place
example: [10,20,30,40,50,60,70,80,90,100]
add [10,30,60,100, 150, 210, 280, 360, 450, 550]

then use binary search get the milestones dates
"""


def binary_search(arr, search):
    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= search and mid -1 >= 0 and arr[mid-1] < search:
            return mid + 1
        
        if arr[mid] < search:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def getMilestoneDays(revenues, milestones):
    result = []
    for i in range(1, len(revenues)):
        revenues[i] += revenues[i-1]
    
    for num in milestones:
        result.append(binary_search(revenues, num))
    
    return result


class TestSolution(unittest.TestCase):
    def test_binary_search_cases(self):
        self.assertEqual(binary_search([10,30,60,100,150,210,280,360,450,550], 200), 6)
    def test_given_cases(self):
        self.assertEqual(getMilestoneDays([10,20,30,40,50,60,70,80,90,100], [100,200,500]), [4, 6, 10])


if __name__ == '__main__':
    unittest.main()


import unittest
"""
Problem:
Suppose we have a list of N numbers, and repeat the following operation until we're left with only a single number: Choose any two numbers and replace them with their sum. Moreover, we associate a penalty with each operation equal to the value of the new number, and call the penalty for the entire list as the sum of the penalties of each operation.
For example, given the list [1, 2, 3, 4, 5], we could choose 2 and 3 for the first operation, which would transform the list into [1, 5, 4, 5] and incur a penalty of 5. The goal in this problem is to find the highest possible penalty for a given input.

Problem Understanding:
1. Basically sum two numbers and replace them with original numbers => add that sum as penalty
2. Repet until only 1 number left
3. return maximum penalty possible from this

Example:
penalty = 0, 7, 9, 10 => 26
[4,2,1,3] => [7,2,1] => [9,1] => [10]

Pseudo code:
sort the array reverse order or use max heap
have penalty = 0
loop sorted array, pop one at a time, add to i-1, update penalty
return penalty

Time complexity => sorting O(nlogn) + loop O(n) => O(nlogn)
Space complexity => O(n) 
"""

def getTotalTime(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    
    sorted_arr = sorted(arr, reverse=True)
    penalty = 0
    for i in range(1, n):
        sorted_arr[i] += sorted_arr[i-1]
        penalty += sorted_arr[i]
    
    return penalty

class TestSolution(unittest.TestCase):
    def test_given_cases(self):
        self.assertEqual(getTotalTime([4,2,1,3]), 26)
        self.assertEqual(getTotalTime([2,3,9,8,4]), 88)

if __name__ == '__main__':
    unittest.main()


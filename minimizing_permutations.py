import unittest
from collections import deque
"""
Problem:
In this problem, you are given an integer N, and a permutation, P of the integers from 1 to N, denoted as (a_1, a_2, ..., a_N). You want to rearrange the elements of the permutation into increasing order, repeatedly making the following operation:
Select a sub-portion of the permutation, (a_i, ..., a_j), and reverse its order.
Your goal is to compute the minimum number of such operations required to return the permutation to increasing order.

Problem Understanding:
- Given an arry, reverse the sub array such that it arranges itself as increasing order, meaning sorted array
Example walk through:
[3,1,2] => (3,1)
[1,3,2] => (3,2)
[1,2,3] => sorted

[1,3,2,4] => (3,2)
[1,2,3,4] => sorted

[5,3,1,4,7,2] => stack [1] => 5,1
[1,3,5,4,7,2] => stack [2] => 5,2
[1,3,2,4,5,7] => stack [2] => 3,2
[1,2,3,4,5,7] => sorted

pseudo code:
queue to keep the edges
result = 0
while True:
    stack = []
    #create edges loop (n)
        check if i < i -1:
            if stack is empty
                add i in stack:
            else:
                see if stack item is > i:
                    swap stack
        if i == n -1:
            add stack to queue
    
    if queue is empty:
        return result

    reverse them
        take out from queue one at a time
        reverse
        result += 1

Time complexity: O(n * n) where n is the length of arr, since nesting the loop, 
Space Complexity : O (1) queue and stack only have one element at a time. 

"""

def minOperations(arr):
    n = len(arr)
    if n == 0:
        return 0
    queue = []
    result = 0

    while True:
        stack = []
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                if len(stack) == 0:
                    stack.append((i-1, i))
                else:
                    if arr[stack[-1][1]] > arr[i]:
                        j = stack.pop()
                        stack.append((j[0],i))
            if i == n -1:
                while stack:
                    queue.append(stack.pop())

        
        if len(queue) == 0:
            return result
        
        while queue:
            i, j = queue.pop()
            arr[i], arr[j] = arr[j], arr[i]
            result += 1

class TestSolution(unittest.TestCase):
    def test_given_cases(self):
        self.assertEqual(minOperations([1,2,5,4,3]), 1)
        self.assertEqual(minOperations([4,1,3,2]),2)
        self.assertEqual(minOperations([3,1,2]), 2)

if __name__ == '__main__':
    unittest.main()


    


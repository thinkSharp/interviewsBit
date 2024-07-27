import unittest
from collections import deque
"""
Problem:
You're given a list of n integers arr, which represent elements in a queue (in order from front to back). You're also given an integer x, and must perform x iterations of the following 3-step process:
Pop x elements from the front of queue (or, if it contains fewer than x elements, pop all of them)
Of the elements that were popped, find the one with the largest value (if there are multiple such elements, take the one which had been popped the earliest), and remove it
For each one of the remaining elements that were popped (in the order they had been popped), decrement its value by 1 if it's positive (otherwise, if its value is 0, then it's left unchanged), and then add it back to the queue
Compute a list of x integers output, the ith of which is the 1-based index in the original array of the element which had been removed in step 2 during the ith iteration.

Solution Approach:
Example: arr = [5,4,7,7,8,9]
x = 5 (3 steps)
return output of the 1 based removed index as the result

pseudo code
result = [] # contains original index + 1 of removed element
loop the arr x time perform 3 steps 

item class:
    index 
    original_val
    modified_val
Convert the arr to the item class

for loop of range(x):
    for loop of items:
        1. Get x num out of loop
        2. find the first max num (record the index)
        3. Remove them 

Time Complexity :
 - item are stored in item then that's O(n)
 - Outer Loop x , finding max of x has O(x) => o(x2) if x < n else o(n2)
Space Complexity: O(len of item)
"""

class Item:
    def __init__(self, index, val) -> None:
        self.index = index + 1
        self.modified_value = val
    
    def modify_val(self):
        if self.modified_value != 0:
            self.modified_value -= 1

def findPositions(arr, x):
    result = []
    items = deque([Item(ind,val) for ind, val in enumerate(arr)])

    
    for _ in range(x):
        temp = deque()
        max = -1
        max_index = -1
        loop_count = min(len(items),x)

        for _ in range(loop_count):
            item = items.popleft()
            if max < item.modified_value:
                max = item.modified_value
                max_index = item.index
            temp.append(item)
        result.append(max_index)

        while temp:
            temp_item = temp.popleft()
            if temp_item.index != max_index:
                temp_item.modify_val()
                items.append(temp_item)

    return result

class TestSolution(unittest.TestCase):
    def test_given_cases(self):
        self.assertEqual(findPositions([1,2,2,3,4,5], 5), [5,6,4,1,2])
        self.assertEqual(findPositions([2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4], 4), [2,5,10,13])


if __name__ == '__main__':
    unittest.main()
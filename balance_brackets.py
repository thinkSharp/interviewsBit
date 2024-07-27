import unittest
"""
Problem:
A bracket is any of the following characters: (, ), {, }, [, or ].
We consider two brackets to be matching if the first bracket is an open-bracket, e.g., (, {, or [, and the second bracket is a close-bracket of the same type. That means ( and ), [ and ], and { and } are the only pairs of matching brackets.
Furthermore, a sequence of brackets is said to be balanced if the following conditions are met:
The sequence is empty, or
The sequence is composed of two or more non-empty sequences, all of which are balanced, or
The first and last brackets of the sequence are matching, and the portion of the sequence without the first and last elements is balanced.
You are given a string of brackets. Your task is to determine whether each sequence of brackets is balanced. If a string is balanced, return true, otherwise, return false

Solution Approach:
Example: '[{}()]' that should be True
Example: '(({[}))' this should be False

Psudo Code:
initialize a stack
loop through the string add them in the stack if they are open brackets. 
Pop them if they are close bracket
we may have to consider special cases if out of order closing bracket appears. then we would return False
At the end of the loop if the stack is empty then it is balance stack

Time Complexity: since it is single loop of s, O(of len s)
Space Complexity: initializing stack with s in worst case so O(of len s)
"""
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, value):
        node = Node(value)
        self.size += 1
        if self.top is not None:
            node.next = self.top
            
        self.top = node

    def pop(self):
        if self.top is not None:
            self.size -= 1
            node = self.top
            self.top = self.top.next
            return node
        
        return None
    
    def seek(self):
        if self.top is not None:
            return self.top.value
        
        return None
    
    
    
def isBalanced(s):
    stack = Stack()
    open_brackets = '({['
    close_brackets = ')}]'
    pair_brackets = '() {} []'
    for item in s:
        if item in open_brackets:
            stack.push(item)
        elif item in close_brackets:
            seek_val = stack.seek()
            if seek_val and seek_val+item in pair_brackets:
                stack.pop()
            else:
                return False

    return stack.size == 0


class TestSolution(unittest.TestCase):
    def test_give_cases(self):
        self.assertEqual(isBalanced('{[()]}'), True)
        self.assertEqual(isBalanced('{}()'), True)
        self.assertEqual(isBalanced('( )'), True)
        self.assertEqual(isBalanced('{(})'), False)


if __name__ == '__main__':
    unittest.main()

            


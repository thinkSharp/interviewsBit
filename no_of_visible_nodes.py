import unittest
from collections import deque

"""
Problem:
There is a binary tree with N nodes. You are viewing the tree from its left side and can see only the leftmost nodes at each level. Return the number of visible nodes.
Note: You can see only the leftmost nodes, but that doesn't mean they have to be left nodes. The leftmost node at a level could be a right node.

Solution Approach:
example: 
                               1
                            2       3
                        4      5        6
                                    7
                                8
what we should see sending from left (1,2,3,7,8)
what we should see sending from right(1,3,6,7,8)

pseudo code:
queue = []
result = []
loop as long as stack is not empty
    layer loop
        first element out append in result
return the result

Time complexity O(n) => number of nodes
space comlexity O(max element in any given layer)
"""
class TreeNode:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.val = key

def visible_nodes(root):
    if root is None:
        return []
    queue = deque()
    result = []
    queue.append(root)
    while queue:
        len_stack = len(queue)
        for i in range(len_stack):
            node = queue.popleft()
            if i == 0:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return len(result)

class TestSolution(unittest.TestCase):
    def setUp(self):
        root_1 = TreeNode(8)
        root_1.left = TreeNode(3)
        root_1.right = TreeNode(10)
        root_1.left.left = TreeNode(1)
        root_1.left.right = TreeNode(6)
        root_1.left.right.left = TreeNode(4)
        root_1.left.right.right = TreeNode(7)
        root_1.right.right = TreeNode(14)
        root_1.right.right.left = TreeNode(13)
        self.root_1 = root_1

        root_2 = TreeNode(10)
        root_2.left = TreeNode(8)
        root_2.right = TreeNode(15)
        root_2.left.left = TreeNode(4)
        root_2.left.left.right = TreeNode(5)
        root_2.left.left.right.right = TreeNode(6)
        root_2.right.left =TreeNode(14)
        root_2.right.right = TreeNode(16)
        self.root_2 = root_2

    
    def test_given_cases(self):
        self.assertEqual(visible_nodes(self.root_2), 5)
        self.assertEqual(visible_nodes(self.root_1), 4)

if __name__ == '__main__':
    unittest.main()


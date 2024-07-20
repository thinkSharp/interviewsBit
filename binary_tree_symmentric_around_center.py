import unittest
"""
Problem Statement:
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Solution Outline:
- First build a binary tree with in_order_traversal from both left and right side of the tree
- in_order_traversal will return list
- will compare both list to see if they are mirror identical
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, node):
        self.root = node
    
    def is_mirror(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and
                self.is_mirror(left.left, right.right) and
                self.is_mirror(left.right, right.left))
    
    def in_order_traversal(self, node, is_left=False):
        if node is None:
            return [-1]
        
        if node.left == None and node.right == None:
            return [node.val]
        
        left_vals = self.in_order_traversal(node.left, True)
        right_vals = self.in_order_traversal(node.right)

        return left_vals + [node.val] + right_vals if is_left else right_vals + [node.val] + left_vals
    
    


class Solution:
    def isSymmetric(self, A):

        if not A:
            return 0
        
        b_tree = BinaryTree(A)


        return 1 if b_tree.is_mirror(b_tree.root.left, b_tree.root.right) else 0
    


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()
    
    def test_simple_binary_tree_case(self):
        node1, node2, node3 = TreeNode(1), TreeNode(2), TreeNode(2)
        node1.left = node2
        node1.right = node3

        self.assertEqual(self.sol.isSymmetric(node1), 1)

    def test_two_layer_b_tree_case(self):
        node1, node2, node3 = TreeNode(1), TreeNode(2), TreeNode(2)
        node1.left = node2
        node1.right = node3

        nodel3, nodel4, noder3, noder4 = TreeNode(3), TreeNode(4), TreeNode(3), TreeNode(4)
        node2.left = nodel3
        node2.right = nodel4

        node3.left = noder4
        node3.right = noder3

        self.assertEqual(self.sol.isSymmetric(node1), 1)

    def test_two_layer_b_tree_case_invalid(self):
        node1, node2, node3 = TreeNode(1), TreeNode(2), TreeNode(2)
        node1.left = node2
        node1.right = node3

        nodel3, nodel4, noder3, noder4 = TreeNode(3), TreeNode(4), TreeNode(3), TreeNode(4)
        node2.right = nodel3

        node3.right = noder3

        self.assertEqual(self.sol.isSymmetric(node1), 0)

if __name__ == '__main__':
    unittest.main()
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self, node=None):
        self.head = node

    
    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def count (self):
        count = 0 if self.head == None else 1
        last_node = self.head
        while last_node.next:
            count += 1
            last_node = last_node.next
        return count
    
    def get_num(self, n):
        if n == 0:
            return self.head.val
        
        count = 0
        last_node = self.head
        while last_node.next:
            count += 1
            if count == n:
                return last_node.val
            last_node = last_node.next
        
        return -1

class Solution:
    """
    Given a linked list A of length N and an integer B.

    You need to find the value of the Bth node from the middle towards the beginning of the Linked List A.

    If no such element exists, then return -1.

    Position of middle node is: (N/2)+1, where N is the total number of nodes in the list.
    """
    def solve(self, A, B):
        ll = LinkedList(A)
        

        count = ll.count()

        mid = (count // 2) + 1

        if mid <= B:
            return -1
        
        return ll.get_num(mid - B)
    

        
    def build_linked_list(self, A):
        ll = LinkedList()
        for item in A:
            ll.append(item)
        return ll
    
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_test_cases(self):
        ll = self.sol.build_linked_list([789])
        self.assertEqual(self.sol.solve(ll.head,1), -1)
        
        ll = self.sol.build_linked_list([468, 335])

        self.assertEqual(self.sol.solve(ll.head,1), 468)

        ll = self.sol.build_linked_list([3,4,7,5,6,16,15,61,16])
        self.assertEqual(self.sol.solve(ll.head,3), 4)

        ll = self.sol.build_linked_list([1,14,6,16,4,10])
        self.assertEqual(self.sol.solve(ll.head,2), 14)

        ll = self.sol.build_linked_list([1,14,6,16,4,10])
        self.assertEqual(self.sol.solve(ll.head, 10), -1)


if __name__ == "__main__":
    unittest.main()

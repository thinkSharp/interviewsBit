import unittest
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self, node=None):
        self.head = node

    def swap_all_pairs(self):
        
        if self.head == None or self.head.next == None:
            return

        dummy = ListNode(0)
        dummy.next = self.head
        prev = dummy
        current = self.head

        while current and current.next:
            first = current
            second = current.next

            #swaping 
            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            current = first.next
        
        self.head = dummy.next
            

    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def to_list(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(current_node.val)
            current_node = current_node.next
        return nodes
    

class Solution:
    def swapPairs(self, A):
        ll = LinkedList(A)
        ll.swap_all_pairs()

        return ll.head
    
    
    def build_linked_list(self, A):
        ll = LinkedList()
        for item in A:
            ll.append(item)
        return ll
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_provided_test_case_one(self):

        ll = self.sol.build_linked_list([1,2,3,5])
        head = self.sol.swapPairs(ll.head)
        lst = LinkedList(head).to_list()
        self.assertEqual(lst, [2,1,5,3])


    def test_provided_test_case_two(self):

        ll = self.sol.build_linked_list([1])
        head = self.sol.swapPairs(ll.head)
        lst = LinkedList(head).to_list()
        self.assertEqual(lst, [1])

    def test_provided_test_case_three(self):

        ll = self.sol.build_linked_list([1,2,3,4,5])
        head = self.sol.swapPairs(ll.head)
        lst = LinkedList(head).to_list()
        self.assertEqual(lst, [2,1,4,3,5])


if __name__ == "__main__":
    unittest.main()




import unittest
from collections import deque, Counter
"""
Problem:
You are given a tree that contains N nodes, each containing an integer u which corresponds to a lowercase character c in the string s using 1-based indexing.
You are required to answer Q queries of type [u, c], where u is an integer and c is a lowercase letter. The query result is the number of nodes in the subtree of node u containing c.

Solution Approach:
Example:
                            a
                        c       a
                    a       b       a
                                a       b

Key thing here is to understand it wants to query multiple time
- that means preprocess once and reuse for all queries

pseudo code:
- build a node to char count which is preprocess 
using BFS: build dictionary of char counter

- then loop through the query to answer them in constant time


Time complexity o(n + Q) 
Space comlexity o(n * C) for each node building a counter 
"""
class Node: 
  def __init__(self, data): 
    self.val = data 
    self.children = []

def dfs(node, s, subtree_count):
    count = Counter()
    count[s[node.val -1]] += 1

    for child in node.children:
        child_count = dfs(child, s, subtree_count)

        for char, cnt in child_count.items():
            count[char] += cnt
    subtree_count[node.val] = count
    return count

def preprocess_tree(root, s):
    subtree_count = {}

    dfs(root, s, subtree_count=subtree_count)
    return subtree_count



def count_of_noes(root, queries, s):
    
    subtree_count = preprocess_tree(root, s)

    result = []
    for u, c in queries:
        result.append(subtree_count[u][c])

    return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        root_1 = Node(1) 
        root_1.children.append(Node(2)) 
        root_1.children.append(Node(3)) 
        self.root_1 = root_1

        root_2 = Node(1)
        root_2.children.append(Node(2))
        root_2.children.append(Node(3))
        root_2.children.append(Node(7))
        root_2.children[0].children.append(Node(4))
        root_2.children[0].children.append(Node(5))
        root_2.children[1].children.append(Node(6))
        self.root_2 = root_2

    def test_given_cases(self):
        self.assertEqual(count_of_noes(self.root_1, [[1,'a']], 'aba'),[2])
        self.assertEqual(count_of_noes(self.root_2,  [[1, 'a'],[2, 'b'],[3, 'a']], 'abaacab'),[4,1,2])


if __name__ == '__main__':
    unittest.main()


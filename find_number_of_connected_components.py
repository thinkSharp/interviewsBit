import unittest
from collections import defaultdict

class ConnectedComponentFinder:
    def __init__(self, A, B):
        self.nodes = A
        self.visited = set()
        self.graph = defaultdict(list)

        for edge in B:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
    
    def dfs(self, node):
        stack = [node]
        while stack:
            current = stack.pop()
            for neighbour in self.graph[current]:
                if neighbour not in self.visited:
                    self.visited.add(neighbour)
                    stack.append(neighbour)

    def find_component(self):
        components = 0
        for node in range(1,self.nodes+1):
            if node not in self.visited:
                components += 1
                self.visited.add(node)
                self.dfs(node)

        return components                   

class Solution:
    """
    Given a graph with A nodes.
    The edges in graph are given in a 2D array B.
    There is an undirected edge between B[i][0] and B[i][1].
    Find the number of connected components in the given graph.
    """
    def solve(self, A,B):
        finder = ConnectedComponentFinder(A, B)
        return finder.find_component()
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_provided_test_cases(self):
        self.assertEqual(self.sol.solve(4, [[1,2],[2,3]]), 2)
        self.assertEqual(self.sol.solve(3, [[1,2],[2,1]]), 2)
        self.assertEqual(self.sol.solve(8,[[1,2],[3,4],[5,6],[7,8]]),4)


if __name__ == '__main__':
    unittest.main()
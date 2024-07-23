import unittest
from collections import defaultdict,OrderedDict
"""
Problem statement:
There are N shops in the street and each shop has only single type of chocolate.

There are M number of children who are willing to pay Xi amount of money only 
if they get the chocolate of their desired type.

Find the total amount earned by all shopkeepers

Solution Outline:
assumption:
N shop contains only quantity of one single type chocolate
child will spend all his money to get that desire chocolate

1. create a dict with type of chocolate with list of shops
2. children finds the desire chocolate type and buy them
   1) Add spent in total amount
   2) Remove the shop from the collection 
"""

class Solution:
    def solve(self):
        N = input()
        T = input()
        C = input()
        money_type_map = []
        for i in range(int(C)):
            money, type = map(int, input().split())
            money_type_map.append((money,type))
        shops = int(N)
        chocolate_types = [int(i) for i in T.split()]
        
        shop_type_map = defaultdict(list)
        for shop, type in enumerate(chocolate_types):
            shop_type_map[type].append(shop)
        
        total = 0

        for money, type in money_type_map:
            shops = shop_type_map[type]
            if len(shops)> 0:
                total += money
                shops.pop(0)
        return total
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.solve())




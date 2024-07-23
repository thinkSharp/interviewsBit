from collections import defaultdict
import itertools

"""
There are N customers who bought items, the list is represent as item id and price.

Your task is to print each item id and total price(quantity * price) in order of its first occurrence.

Solution outline:
1). Item could have different prices
2). default dictionary of item and add prices
3) print the output
"""

class Solution:
    def solve(self):
        N = int(input())
        item_total_price_map = defaultdict(int)
        for _ in range(N):
            item, total = map(int, input().split())
            item_total_price_map[item] += total
        
        for item, price in item_total_price_map.items():
            print(f'{item} {price}')
    
if __name__ == '__main__':
    sol = Solution()
    sol.solve()
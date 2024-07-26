import unittest
"""
Problem:
You likely know that different currencies have coins and bills of different denominations. In some currencies, it's actually impossible to receive change for a given amount of money. For example, Canada has given up the 1-cent penny. If you're owed 94 cents in Canada, a shopkeeper will graciously supply you with 95 cents instead since there exists a 5-cent coin.
Given a list of the available denominations, determine if it's possible to receive exact change for an amount of money targetMoney. Both the denominations and target amount will be given in generic units of that currency.

solution approach:
example 1: [1,5,10,20,50,100], target = 95, 94
example 2: [4,7,17,29], target = 63,
because we need to try multiple different posibilities, recursion should be a good choice

psudo code:

if target < demonator[0]: return false
if target == 0 : return true

loop of denomators
    if  target // denomator[i]:
        return_val |= call the same function (target - denomator[i])

return return_val
"""

def get_exact_change(target_money, denominations, memo):

    if target_money in memo:
        return memo[target_money]
    
    if target_money == 0:
        return True
    
    if target_money < denominations[0]:
        return False
    
    return_val = False
    for denom in reversed(denominations):
        if target_money // denom:
            remainder = target_money % denom
            if remainder >= 0 and  get_exact_change(remainder, denominations, memo):
                memo[target_money] = True
                return True
            
    memo[target_money] = False
    return False
 
def canGetExactChange(targetMoney, denominations):
    memo = {}
    return get_exact_change(target_money=targetMoney, denominations=denominations, memo=memo)


"""
Time Complexity: each possible of target_money is solve once due to memo O(Denom * t) 
Space Complexity: O(M) for memo and O(M) for stack therefor it is O(M)
"""

class TestSolution(unittest.TestCase):
    def test_get_exact_chage_cases(self):
        self.assertEqual(get_exact_change(50, [1,5,10], {}), True)

    def test_given_cases(self):
        self.assertEqual(canGetExactChange(94, [5,10,25,100,200]), False)
        self.assertEqual(canGetExactChange(75, [4,17,29]), True)


if __name__ == '__main__':
    unittest.main()


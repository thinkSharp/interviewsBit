import unittest
import math
"""
Problem:
We have N different apps with different user growth rates. At a given time t, measured in days, the number of users using an app is g^t (for simplicity we'll allow fractional users), where g is the growth rate for that app. These apps will all be launched at the same time and no user ever uses more than one of the apps. We want to know how many total users there are when you add together the number of users from each app.
After how many full days will we have 1 billion total users across the N apps?

Solution Scope:
based on the growth rate, we will have to calculate no. of days
example: 1 = 1, 2 = 1.5, 3 = 1.5^3 
calculate the growth rate by increment of 20 days
calculate the population for a given date
will also have binary search function that will return the date
"""
def calculate_population_for_a_given_date(rates, date):
    total = 0.0
    for rate in rates:
        total += rate ** date
    return total

def binary_search(dates, search):
    n = len(dates)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if dates[mid] >= search and mid - 1 >= 0 and dates[mid-1] < search:
            return mid
        
        if dates[mid] < search:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def getBillionUsersDay(growthRates):
    billion_user = 1000000000
    left , right = 0, 5000
    frequency = 10
    date = 0
    while True:
        date += frequency
        population = calculate_population_for_a_given_date(growthRates, date)
        
        if population < billion_user:
            left = date
        else:
            right = date
            break
    
    dates = []
    for i in range(left, right+1):
        dates.append(calculate_population_for_a_given_date(growthRates, i))
    
    result = binary_search(dates, billion_user)

    return result + left

class TestSolution(unittest.TestCase):
    def test_calculate_population_for_given_date_cases(self):
        self.assertEqual(calculate_population_for_a_given_date([1.5], 3), 3.375)

    def test_binary_search_cases(self):
        self.assertEqual(binary_search([10,20,30,40,50,60],35), 3)

    
    def test_give_cases(self):
        self.assertEqual(getBillionUsersDay([1.5]), 52)
        self.assertEqual(getBillionUsersDay([1.1,1.2,1.3]), 79)
        self.assertEqual(getBillionUsersDay([1.01,1.02]), 1047)


if __name__ == '__main__':
    unittest.main()

        



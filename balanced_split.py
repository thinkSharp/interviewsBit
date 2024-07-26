import unittest

"""
Question:
Given an array of integers (which may include repeated integers), determine if there's a way to split the array into two subsequences A and B such that the sum of the integers in both arrays is the same, and all of the integers in A are strictly smaller than all of the integers in B.
Note: Strictly smaller denotes that every integer in A must be less than, and not equal to, every integer in B.

Solution Aproach:
1. Sort
2. add previous value in yourself
3. search for a split point (linear)
    all element in left sorted must be less then right
4. return

Example: 
[1,5,7,1]
[1,1,5,7]
[1,2,7,14]
if a[i] == a[len(a) - 1] - a[i]:
    return true

return false
"""

def merge_sort(arr):
    if not arr:
        return arr
    
    left = 0
    right = len(arr) 
    result = merge_sort_arrays(arr[left:right])
    return result

def merge_sort_arrays(arr):

    right = len(arr)
    
    if right <= 1:
        return arr
    
    mid =  right // 2

    left_array = merge_sort_arrays(arr[: mid])
    right_array = merge_sort_arrays(arr[mid:])

    result = merge_sub_arrays(left_array, right_array)

    return result

def merge_sub_arrays(left_array, right_array):
    result = []
    left_len = len(left_array)
    right_len = len(right_array)
    i, j = 0, 0
    while i < left_len and j < right_len:
        if left_array[i] < right_array[j]:
            result.append(left_array[i])
            i += 1
        else:
            result.append(right_array[j])
            j += 1
    while i < left_len:
        result.append(left_array[i])
        i += 1
    
    while j < right_len:
        result.append(right_array[j])
        j += 1
    
    return result

def balancedSplitExists(arr):
    sorted_arr = merge_sort(arr)

    sorted_arr_clone = sorted_arr[:]
    for i in range(1, len(sorted_arr)):
        sorted_arr[i] += sorted_arr[i-1]

    last_element = sorted_arr[len(sorted_arr)-1] // 2
    for i in range(0, len(sorted_arr) -1):
        if sorted_arr[i] == last_element and sorted_arr_clone[i] < sorted_arr_clone[i+1]:
            return True
    return False


class TestSolution(unittest.TestCase):
    def test_merge_sort(self):
        self.assertEqual(merge_sort([5,4,3]), [3,4,5])
        self.assertEqual(merge_sort([5,4,3,17,5,8,2,9]), [2,3,4,5,5,8,9,17])

    def test_given_cases(self):
        self.assertEqual(balancedSplitExists([2,1,2,5]), True)
        self.assertEqual(balancedSplitExists([3,6,3,4,4]), False)
        self.assertEqual(balancedSplitExists([1,5,7,1]), True)
        self.assertEqual(balancedSplitExists([1111]), False)
        self.assertEqual(balancedSplitExists([12,7,6,7,6]), False)

if __name__ == '__main__':
    unittest.main()




    
    

    
import unittest
"""
problem:
You've devised a simple encryption method for alphabetic strings that shuffles the characters in such a way that the resulting string is hard to quickly read, but is easy to convert back into the original string.
When you encrypt a string S, you start with an initially-empty resulting string R and append characters to it as follows:
Append the middle character of S (if S has even length, then we define the middle character as the left-most of the two central characters)
Append the encrypted version of the substring of S that's to the left of the middle character (if non-empty)
Append the encrypted version of the substring of S that's to the right of the middle character (if non-empty)
For example, to encrypt the string "abc", we first take "b", and then append the encrypted version of "a" (which is just "a") and the encrypted version of "c" (which is just "c") to get "bac".
If we encrypt "abcxcba" we'll get "xbacbca". That is, we take "x" and then append the encrypted version "abc" and then append the encrypted version of "cba".

Solution Outline:
I am thinking this as a recursion problem.
Example: of 3 chars abc => bac first take middle character 
Example: of 4 chars abcd => bacd => take left most bacd
Example: of 5 chars abcde => cabde => c is middle, left and right after encryption remain the same
Example: of 6 chars abcdef => cabedf
Example: of 7 chars abcdefg => dbacfeg
Example: 0f 8 chars facebook => efacbook => e => left fac => afc and right is book => obok => eafcobok

code:
recursive function:
divide the string into two,
- base cases: len less then 2 return
- handle even and odd strings differently and call recursive function
- merge the outcome
"""
def encrypt_word(s):
    n = len(s)
    if n <= 2:
        return s
    mid = n // 2
    is_odd = mid % 2
    
    if not is_odd:
        mid = mid - 1

    middle_char = s[mid]
    left_s = encrypt_word(s[:mid])
    right_s = encrypt_word(s[mid+1:])

    return middle_char + left_s + right_s
   
def findEncryptedWord(s):
    return encrypt_word(s)

class TestSolution(unittest.TestCase):
    def test_encrypt_word_cases(self):
        self.assertEqual(encrypt_word('abc'), 'bac')

    def test_given_cases(self):
        self.assertEqual(findEncryptedWord('abcd'), 'bacd')
        self.assertEqual(findEncryptedWord('abcxcba'), 'xbacbca')
        self.assertEqual(findEncryptedWord('facebook'),'eafcobok')

"""
time complexity = O (s)
space complexity = O(s) because of recursion
"""
if __name__ == '__main__':
    unittest.main()
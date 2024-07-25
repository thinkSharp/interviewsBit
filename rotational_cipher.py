import unittest
"""
Problem Statement:
One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.
Given a string and a rotation factor, return an encrypted string.

Solution Approach:

in a given string, rotation will happen on 3 different set of number. 
Upper Case, Lower Case, Numeric => ASCII no.
A-Z if beyond Z then remove Z and start from A
a-z if beyond z then remove z and start from A
1-0 if beyond 0 then remove 0 and start from 1
"""

class Solution:
    def rotate_a_char(self,ch, factor):
        if 'a' <= ch <= 'z':
            return chr((ord(ch) - ord('a') + factor) % 26 + ord('a'))
        elif 'A' <= ch <= 'Z':
            return chr((ord(ch) - ord('A') + factor) % 26 + ord('A'))
        elif '0' <= ch <= '9':
            return chr((ord(ch) - ord('0') + factor) % 10 + ord('0'))
        else:
            return ch

            
    def rotationalCipher(self, input_str, rotation_factor):
        result = [self.rotate_a_char(ch, rotation_factor) for ch in input_str]
        return ''.join(result)
    
class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.rotate_a_char('9', 200), '9')
        self.assertEqual(self.sol.rotationalCipher('abcdZXYzxy-999.@', 200), 'stuvRPQrpq-999.@')
        self.assertEqual(self.sol.rotationalCipher('All-convoYs-9-be:Alert1.',4), 'Epp-gsrzsCw-3-fi:Epivx5.')
        self.assertEqual(self.sol.rotationalCipher('Zebra-493',3), 'Cheud-726')

if __name__ == '__main__':
    unittest.main()
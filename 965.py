"""
This problem was asked by Google.
UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.
For example, the Euro sign, €, corresponds to the three bytes 11100010 10000010 10101100. The rules for mapping characters are as follows:
•	For a single-byte character, the first bit must be zero.
•	For an n-byte character, the first byte starts with n ones and a zero. The other n - 1 bytes all start with 10.
Visually, this can be represented as follows.
 Bytes   |           Byte format
-----------------------------------------------
   1     | 0xxxxxxx
   2     | 110xxxxx 10xxxxxx
   3     | 1110xxxx 10xxxxxx 10xxxxxx
   4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Write a program that takes in an array of integers representing byte values, and returns whether it is a valid UTF-8 encoding.
"""
# research for the problem
# note: UTF-8 is designed for backward compatiability with ASCII, and the first byte of is reserved for the first 128 ASCII characters
# rule: single byte charaters starts with 0, n-byte characters starts with n-ones and a zero while the other bytes start with 10

import unittest

# assumes input will always be correct byte format, ie. sequences of 8 bit integers and numbers of sequences
def is_utf8(integer_array):
    if type(integer_array) == str: # supports string format for input
        integer_array = [int(i) for i in integer_array if i != " "]
    
    bytes_ = 8 # bits
    if len(integer_array) == bytes_:    # can this be optimized?
        return integer_array[0] == 0
    if len(integer_array) == 2 * bytes_:
        return integer_array[:3] == [1, 1, 0] and integer_array[8:10] == [1, 0]
    if len(integer_array) == 3 * bytes_:
        return integer_array[:4] == [1, 1, 1, 0] and integer_array[8:10] == [1, 0] and integer_array[16:18] == [1, 0]
    if len(integer_array) == 4 * bytes_:
        return integer_array[:5] == [1, 1, 1, 1, 0] and integer_array[8:10] == [1, 0] and integer_array[16:18] == [1, 0] and integer_array[24: 26] == [1, 0]
    
    

class Test(unittest.TestCase):
    def test_given(self):
        self.assertTrue(is_utf8([1,1,1,0,0,0,1,0, 1,0,0,0,0,0,1,0, 1,0,1,0,1,1,0,0]))
        self.assertTrue(is_utf8("11100010 10000010 10101100"))
    def test_one_byte(self):
        self.assertTrue(is_utf8([0,0,0,0,0,0,0,0]))
        self.assertTrue(is_utf8("00000000"))
    def test_one_byte_fail(self):
        self.assertFalse(is_utf8([1,0,0,0,0,0,0,0]))
        self.assertFalse(is_utf8("10000000"))
    def test_two_byte(self):
        self.assertTrue(is_utf8([1,1,0,0,0,0,0,0, 1,0,0,0,0,0,0,0]))
        self.assertTrue(is_utf8("11000000 10000000"))
    def test_two_byte_fail(self):
        self.assertFalse(is_utf8([0,1,0,0,0,0,0,0, 0,1,1,1,1,1,1,1]))
        self.assertFalse(is_utf8("01000000 01111111"))
    def test_three_byte(self):
        self.assertTrue(is_utf8([1,1,1,0,0,0,0,0, 1,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0]))
        self.assertTrue(is_utf8("11100000 10000000 10000000"))
    def test_three_byte_fail(self):
        self.assertFalse(is_utf8([0,1,1,1,1,1,1,1, 0,1,1,1,1,1,1,1, 0,1,1,1,1,1,1,1,1]))
        self.assertFalse(is_utf8("01111111 01111111 011111111"))
    def test_four_byte(self):
        self.assertTrue(is_utf8([1,1,1,1,0,0,0,0, 1,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0]))
        self.assertTrue(is_utf8("11110000 10000000 10000000 10000000"))
    def test_four_byte_fail(self):
        self.assertFalse(is_utf8([0,1,1,1,1,1,1,1, 0,1,1,1,1,1,1,1, 0,1,1,1,1,1,1,1, 0,1,1,1,1,1,1,1,1]))
        self.assertFalse(is_utf8("01111111 01111111 01111111 011111111"))
    def test_edge(self):
        self.assertFalse(is_utf8([1,1,0,0,0,0,0,1, 0,0,0,0,0,0,0,1]))
        self.assertFalse(is_utf8("11000001 00000001"))
if __name__ == "__main__":
    unittest.main()
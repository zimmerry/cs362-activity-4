import unittest
import pytest
import palindrome

class TestPalindromeMethods(unittest.TestCase):
    def test1(self):
        self.assertEqual(palindrome.is_palindrome('racecar'), True)

    def test2(self):
        self.assertEqual(palindrome.is_palindrome('this is not a palindrome'), False)

    def test3(self):
        self.assertEqual(palindrome.is_palindrome('kayak'), True)

class TestPalindromeClass:
    def test_one(self):
        assert palindrome.is_palindrome('racecar') == True

    def test_two(self):
        assert palindrome.is_palindrome('this is not a palindrome') == False

    def test_three(self):
        assert palindrome.is_palindrome('kayak') == True

if __name__ == '__main__':
    unittest.main()
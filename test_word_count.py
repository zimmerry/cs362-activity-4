import unittest
import pytest
import word_count

class TestWordCountMethods(unittest.TestCase):
    def test1(self):
        self.assertEqual(word_count.get_word_count('This is a sentence'), 4)

    def test2(self):
        self.assertEqual(word_count.get_word_count('Word'), 1)

    def test3(self):
        self.assertEqual(word_count.get_word_count('     '), 0)

class TestWordCountClass:
    def test_one(self):
        assert word_count.get_word_count('This is a sentence') == 4

    def test_two(self):
        assert word_count.get_word_count('Word') == 1

    def test_three(self):
        assert word_count.get_word_count('     ') == 0

if __name__ == '__main__':
    unittest.main()
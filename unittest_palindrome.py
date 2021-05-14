import palindrome
import unittest

class SimpleTest(unittest.TestCase):

    def test_tacocat(self):
        self.assertTrue(palindrome.check_palindrome("tacocat"))

    def test_tacodog(self):
        self.assertFalse(palindrome.check_palindrome("tacodog"))

    def test_racecar(self):
        self.assertTrue(palindrome.check_palindrome("racecar"))

if __name__ == '__main__':
    unittest.main()

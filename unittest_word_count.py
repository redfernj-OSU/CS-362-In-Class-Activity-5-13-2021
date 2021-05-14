import word_count
import unittest

class SimpleTest(unittest.TestCase):

    def test_tacocat(self):
        self.assertEqual(word_count.word_length("taco cat"), 2)

    def test_test_Sentence1(self):
        self.assertEqual(word_count.word_length("Hello my name is Jacob Redfern."), 6)

    def test_test_Sentence2(self):
        self.assertEqual(word_count.word_length("This is an in class activity."), 6)

if __name__ == '__main__':
    unittest.main()

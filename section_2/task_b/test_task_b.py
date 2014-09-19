import unittest

from task_b import is_palindrome


class TaskBTests(unittest.TestCase):

    def test_returns_true_for_single_letter(self):
        word = 'a'

        res = is_palindrome(word)

        self.assertTrue(res)

    def test_returns_false_for_empty_string(self):
        word = ''

        res = is_palindrome(word)

        self.assertFalse(res)

    def test_returns_true_for_odd_lettered_palindrome(self):
        word = 'radar'

        res = is_palindrome(word)

        self.assertTrue(res)

    def test_returns_true_for_even_lettered_palindrome(self):
        word = 'anna'

        res = is_palindrome(word)

        self.assertTrue(res)

    def test_removes_punctuation(self):
        word = '\'.,!-:"?'

        res = is_palindrome(word)

        self.assertFalse(res)

    def test_returns_true_for_palindrome_sentance(self):
        word = 'amore, roma.'

        res = is_palindrome(word)

        self.assertTrue(res)

    def test_returns_true_for_capitalised_palindrome_sentance(self):
        word = 'Amore, Roma.'

        res = is_palindrome(word)

        self.assertTrue(res)

    def test_returns_false_for_non_palindrome(self):
        word = 'foobar'

        res = is_palindrome(word)

        self.assertFalse(res)

    def test_removes_newlines(self):
        word = 'A but tuba.\n'

        res = is_palindrome(word)

        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()

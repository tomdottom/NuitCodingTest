import unittest

from task_d import word_count


class TaskDTests(unittest.TestCase):

    def test_empty_list_outputs_empty_dict(self):
        list = []

        res = word_count(list)

        self.assertEqual(res, {})

    def test_single_word_ouputs_single_dict_item(self):
        list = ['one']

        res = word_count(list)

        self.assertEqual(res, {'one': 1})

    def test_ignores_empty_strings(self):
        list = ['one', '', 'one']

        res = word_count(list)

        self.assertEqual(res, {'one': 2})

    def test_on_large_list(self):
        list = [
            'one', 'two', 'three', 'four', 'five', 'six',
            'one', 'two', 'three', 'four', 'five',
            'one', 'two', 'three', 'four',
            'one', 'two', 'three',
            'one', 'two',
            'one',
        ]

        res = word_count(list)

        self.assertEqual(
            res,
            {
                'six': 1,
                'five': 2,
                'four': 3,
                'three': 4,
                'two': 5,
                'one': 6
            }
        )


if __name__ == '__main__':
    unittest.main()

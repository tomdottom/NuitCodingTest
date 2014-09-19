import unittest

from task_e import make_family_tree


class TaskETests(unittest.TestCase):

    def test_returns_single_induvidual(self):
        orphan = '[{"id": 1, "parent": null}]'

        res = make_family_tree(orphan)

        self.assertEqual(res, orphan)

    def test_pair_child_with_parent(self):
        child_parent = '[{"id": 1, "parent": null}, {"id": 2, "parent": 1}]'

        res = make_family_tree(child_parent)

        self.assertEqual(
            res,
            '[{"sons": [2], "id": 1, "parent": null}, {"id": 2, "parent": 1}]'
        )

    def test_pair_two_children_with_parent(self):
        child_parent = (
            '[{"id": 1, "parent": null}, {"id": 2, "parent": 1}, '
            '{"id": 3, "parent": 1}]')

        res = make_family_tree(child_parent)

        self.assertEqual(
            res,
            '[{"sons": [2, 3], "id": 1, "parent": null}, '
            '{"id": 2, "parent": 1}, {"id": 3, "parent": 1}]'
        )

    def test_given_induviduals_returns_family(self):
        familes_as_json = (
            '['
                '{"id": 1, "parent": 2},'
                '{"id": 2, "parent": null},'
                '{"id": 3, "parent": 2},'
                '{"id": 4, "parent": 5},'
                '{"id": 5, "parent": null}'
            ']'
        )

        result = make_family_tree(familes_as_json)

        self.assertEqual(
            result,
            '['
                '{"id": 1, "parent": 2}, '
                '{"sons": [1, 3], "id": 2, "parent": null}, '
                '{"id": 3, "parent": 2}, '
                '{"id": 4, "parent": 5}, '
                '{"sons": [4], "id": 5, "parent": null}'
            ']'
        )


if __name__ == '__main__':
    unittest.main()

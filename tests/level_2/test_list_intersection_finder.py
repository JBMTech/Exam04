
import unittest
from src.level_2.py_list_intersection_finder import list_intersection_finder


class TestListIntersectionFinder(unittest.TestCase):

    def test_common_elements(self):
        self.assertEqual(
            list_intersection_finder([
                [1, 2, 3],
                [2, 3, 4],
                [2, 3, 5]
            ]),
            [2, 3]
        )

    def test_single_common_element(self):
        self.assertEqual(
            list_intersection_finder([
                [1, 2, 3, 4],
                [2, 4, 6, 8],
                [4, 8, 12]
            ]),
            [4]
        )

    def test_duplicate_elements(self):
        self.assertEqual(
            list_intersection_finder([
                [1, 1, 2, 3],
                [1, 2, 2, 3],
                [1, 2, 3, 3]
            ]),
            [1, 2, 3]
        )

    def test_no_common_elements(self):
        self.assertEqual(
            list_intersection_finder([
                [1, 2, 3],
                [4, 5, 6]
            ]),
            []
        )

    def test_empty_input(self):
        self.assertEqual(
            list_intersection_finder([]),
            []
        )

    def test_one_empty_list(self):
        self.assertEqual(
            list_intersection_finder([
                [1, 2, 3],
                []
            ]),
            []
        )

    def test_single_list(self):
        self.assertEqual(
            list_intersection_finder([[5]]),
            [5]
        )


if __name__ == "__main__":
    unittest.main()

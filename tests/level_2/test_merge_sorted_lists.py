
import unittest
from src.level_2.py_merge_sorted_lists import merge_sorted_lists


class TestMergeSortedLists(unittest.TestCase):

    def test_merge_two_sorted_lists(self):
        self.assertEqual(
            merge_sorted_lists([[1, 3, 5], [2, 4, 6]]),
            [1, 2, 3, 4, 5, 6]
        )

    def test_merge_three_sorted_lists(self):
        self.assertEqual(
            merge_sorted_lists([
                [1, 5, 9],
                [2, 3, 8],
                [4, 6, 7]
            ]),
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        )

    def test_merge_lists_of_different_lengths(self):
        self.assertEqual(
            merge_sorted_lists([[5], [1, 3], [2, 4]]),
            [1, 2, 3, 4, 5]
        )

    def test_merge_with_duplicates(self):
        self.assertEqual(
            merge_sorted_lists([[1, 1, 2], [2, 3, 3]]),
            [1, 1, 2, 2, 3, 3]
        )

    def test_merge_with_empty_list(self):
        self.assertEqual(
            merge_sorted_lists([[], [1, 2, 3]]),
            [1, 2, 3]
        )

    def test_only_empty_lists(self):
        self.assertEqual(
            merge_sorted_lists([[]]),
            []
        )

    def test_merge_negative_numbers(self):
        self.assertEqual(
            merge_sorted_lists([
                [-5, -1, 0],
                [-3, 2, 4]
            ]),
            [-5, -3, -1, 0, 2, 4]
        )

    def test_merge_identical_elements(self):
        self.assertEqual(
            merge_sorted_lists([[10], [10], [10]]),
            [10, 10, 10]
        )


if __name__ == "__main__":
    unittest.main()


import unittest
from src.level_4.py_sliding_window_maximum import sliding_window_maximum


class TestSlidingWindowMaximum(unittest.TestCase):

    def test_standard_case(self):
        self.assertEqual(
            sliding_window_maximum(
                [1, 3, -1, -3, 5, 3, 6, 7], 3
            ),
            [3, 3, 5, 5, 6, 7]
        )

    def test_window_size_two(self):
        self.assertEqual(
            sliding_window_maximum([1, 2, 3, 4, 5], 2),
            [2, 3, 4, 5]
        )

    def test_window_size_one(self):
        self.assertEqual(
            sliding_window_maximum([5, 4, 3, 2, 1], 1),
            [5, 4, 3, 2, 1]
        )

    def test_window_equals_list_length(self):
        self.assertEqual(
            sliding_window_maximum([1, 2, 3], 3),
            [3]
        )

    def test_window_larger_than_list(self):
        self.assertEqual(
            sliding_window_maximum([1, 2, 3], 4),
            []
        )

    def test_empty_list(self):
        self.assertEqual(
            sliding_window_maximum([], 2),
            []
        )

    def test_window_size_zero(self):
        self.assertEqual(
            sliding_window_maximum([1, 2, 3], 0),
            []
        )


if __name__ == "__main__":
    unittest.main()

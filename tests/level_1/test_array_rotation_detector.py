
import unittest
from src.level_1.py_array_rotation_detector import array_rotation_detector


class TestArrayRotationDetector(unittest.TestCase):

    def test_rotation_left(self):
        self.assertTrue(
            array_rotation_detector(
                [1, 2, 3, 4, 5],
                [4, 5, 1, 2, 3]
            )
        )

    def test_rotation_right(self):
        self.assertTrue(
            array_rotation_detector(
                [1, 2, 3, 4, 5],
                [5, 1, 2, 3, 4]
            )
        )

    def test_not_a_rotation(self):
        self.assertFalse(
            array_rotation_detector(
                [1, 2, 3],
                [3, 2, 1]
            )
        )

    def test_different_lengths(self):
        self.assertFalse(
            array_rotation_detector(
                [1, 2],
                [1, 2, 3]
            )
        )

    def test_empty_lists(self):
        self.assertTrue(
            array_rotation_detector([], [])
        )


if __name__ == "__main__":
    unittest.main()

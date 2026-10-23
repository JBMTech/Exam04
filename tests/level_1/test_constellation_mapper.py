
import unittest
from src.level_1.py_constellation_mapper import constellation_mapper


class TestConstellationMapper(unittest.TestCase):

    def test_diagonal_constellation(self):
        self.assertEqual(
            constellation_mapper([(0, 0), (1, 1), (2, 2)], 3),
            ['*..', '.*.', '..*']
        )

    def test_cross_constellation(self):
        self.assertEqual(
            constellation_mapper(
                [(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3
            ),
            ['.*.', '***', '.*.']
        )

    def test_empty_constellation(self):
        self.assertEqual(
            constellation_mapper([], 2),
            ['..', '..']
        )

    def test_duplicate_coordinates(self):
        self.assertEqual(
            constellation_mapper([(0, 0), (0, 0), (1, 1)], 2),
            ['*.', '.*']
        )

    def test_coordinates_out_of_bounds(self):
        self.assertEqual(
            constellation_mapper([(0, 0), (5, 5)], 3),
            ['*..', '...', '...']
        )

    def test_horizontal_constellation(self):
        self.assertEqual(
            constellation_mapper([(1, 0), (1, 1), (1, 2)], 3),
            ['...', '***', '...']
        )


if __name__ == "__main__":
    unittest.main()

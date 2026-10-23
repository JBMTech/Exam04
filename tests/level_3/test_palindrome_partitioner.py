
import unittest
from src.level_3.py_palindrome_partitioner import palindrome_partitioner


class TestPalindromePartitioner(unittest.TestCase):

    def test_aab(self):
        self.assertEqual(
            palindrome_partitioner("aab"),
            1
        )

    def test_aba(self):
        self.assertEqual(
            palindrome_partitioner("aba"),
            0
        )

    def test_abc(self):
        self.assertEqual(
            palindrome_partitioner("abc"),
            2
        )


if __name__ == "__main__":
    unittest.main()


import unittest
from src.level_3.py_package_dependency_resolver import package_dependency_resolver


class TestPackageDependencyResolver(unittest.TestCase):

    def test_simple_dependency_chain(self):
        self.assertEqual(
            package_dependency_resolver({
                "app": ["database"],
                "database": ["driver"],
                "driver": []
            }),
            ["driver", "database", "app"]
        )

    def test_multiple_dependencies(self):
        self.assertEqual(
            package_dependency_resolver({
                "A": [],
                "B": ["A"],
                "C": ["A", "B"]
            }),
            ["A", "B", "C"]
        )

    def test_empty_dependencies(self):
        self.assertEqual(
            package_dependency_resolver({}),
            []
        )

    def test_circular_dependency(self):
        self.assertEqual(
            package_dependency_resolver({
                "X": ["Y"],
                "Y": ["X"]
            }),
            []
        )

    def test_independent_packages(self):
        self.assertEqual(
            package_dependency_resolver({
                "web": [],
                "api": [],
                "frontend": ["web"],
                "backend": ["api"]
            }),
            ["api", "web", "backend", "frontend"]
        )


if __name__ == "__main__":
    unittest.main()

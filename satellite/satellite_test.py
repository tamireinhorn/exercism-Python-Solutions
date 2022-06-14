import unittest

from satellite import (
    tree_from_traversals,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class SatelliteTest(unittest.TestCase):
    def test_empty_tree(self):
        preorder = []
        inorder = []

        expected = {}
        self.assertEqual(tree_from_traversals(preorder, inorder), expected)

    def test_tree_with_one_item(self):
        preorder = ["a"]
        inorder = ["a"]

        expected = {"v": "a", "l": {}, "r": {}}
        self.assertEqual(tree_from_traversals(preorder, inorder), expected)

    def test_tree_with_many_items(self):
        preorder = ["a", "i", "x", "f", "r"]
        inorder = ["i", "a", "f", "x", "r"]

        expected = {
            "v": "a",
            "l": {"v": "i", "l": {}, "r": {}},
            "r": {
                "v": "x",
                "l": {"v": "f", "l": {}, "r": {}},
                "r": {"v": "r", "l": {}, "r": {}},
            },
        }
        self.assertEqual(tree_from_traversals(preorder, inorder), expected)

    def test_simple_tree(self):
        inorder = ["1", "2"]
        preorder = ["2", "1"]

        expected = {
            "v": "2",
            "l": "1",
            "r": {}
        }
        self.assertEqual(tree_from_traversals(preorder, inorder), expected)

    def test_complex_tree(self):
        inorder = ["1", "2", "3", "5", "6", "7"]
        preorder = ['2', '1', '3', '6', '5', '7']
        expected = { "v": "4", 
                    "l": {"v": "2", 
                            "l": {"v": "1", "l": {}, "r": {}},
                            "r": {"v": "3", "l": {}, "r": {}}},
                    "r": {"v": "6",
                            "l": {"v": "5", "l": {}, "r": {}},
                            "r": {"v": "7", "l": {}, "r": {}}
                    }

        }
        self.assertEqual(tree_from_traversals(preorder, inorder), expected)

    def test_reject_traversals_of_different_length(self):
        preorder = ["a", "b"]
        inorder = ["b", "a", "r"]

        with self.assertRaises(ValueError) as err:
            tree_from_traversals(preorder, inorder)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "traversals must have the same length")

    def test_reject_inconsistent_traversals_of_same_length(self):
        preorder = ["x", "y", "z"]
        inorder = ["a", "b", "c"]

        with self.assertRaises(ValueError) as err:
            tree_from_traversals(preorder, inorder)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(
            err.exception.args[0], "traversals must have the same elements"
        )

    def test_reject_traversals_with_repeated_items(self):
        preorder = ["a", "b", "a"]
        inorder = ["b", "a", "a"]

        with self.assertRaises(ValueError) as err:
            tree_from_traversals(preorder, inorder)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "traversals must contain unique items")

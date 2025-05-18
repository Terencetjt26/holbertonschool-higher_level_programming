#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 7, 6, 3]), 9)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-3, -2, -1, -5]), -1)

    def test_mixed_positive_and_negative(self):
        self.assertEqual(max_integer([-10, 20, -30, 40, 0]), 40)

    def test_all_equal_elements(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.3, 3.7, 2.8]), 3.7)

    def test_mixed_ints_and_floats(self):
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)

    def test_string_input(self):
        self.assertEqual(max_integer("hello"), "o")

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_list_with_none(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, None])

    def test_list_with_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])


if __name__ == '__main__':
    unittest.main()

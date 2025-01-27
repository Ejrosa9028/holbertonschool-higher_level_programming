#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer function"""

    def test_max_integer_normal_case(self):
        """Test normal case with a list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_integer_single_element(self):
        """Test case with a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_max_integer_empty_list(self):
        """Test case with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_max_integer_with_negative_numbers(self):
        """Test case with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_integer_all_equal(self):
        """Test case where all elements are the same"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_max_integer_mixed_numbers(self):
        """Test case with mixed positive and negative numbers"""
        self.assertEqual(max_integer([10, -5, 4, -2]), 10)

    def test_max_integer_large_numbers(self):
        """Test case with large numbers"""
        self.assertEqual(max_integer([1000000, 5000000, 3000000]), 5000000)

if __name__ == "__main__":
    unittest.main()

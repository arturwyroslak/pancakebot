import unittest

from src.some_file import new_method


class TestNewMethod(unittest.TestCase):

    def test_new_method_valid_input(self):
        self.assertEqual(new_method(1, 2, 3), expected_output)

    def test_new_method_invalid_input(self):
        with self.assertRaises(ValueError):
            new_method('invalid', 2, 3)

    def test_new_method_edge_cases(self):
        self.assertEqual(new_method(0, 0, 0), expected_output)
        self.assertEqual(new_method(-1, -2, -3), expected_output)
        self.assertEqual(new_method(2147483647, 2147483647, 2147483647), expected_output)

if __name__ == '__main__':
    unittest.main()

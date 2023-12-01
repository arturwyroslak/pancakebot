import unittest
from unittest.mock import patch

from src import some_module


class TestSomeModule(unittest.TestCase):

    @patch('src.some_module.new_method')
    def test_new_method(self, mock_new_method):
        # Mock the return value of the new method
        mock_new_method.return_value = True

        # Call the function that uses the new method
        result = some_module.function_that_uses_new_method()

        # Assert the new method was called with the correct arguments
        mock_new_method.assert_called_once_with(var1, var2, var3)

        # Assert the function returned the expected result
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()

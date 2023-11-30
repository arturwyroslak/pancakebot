```python
import unittest
from unittest.mock import patch
from src import user_interface

class TestUserInterface(unittest.TestCase):

    @patch('src.user_interface.customize_UI')
    def test_customize_UI(self, mock_customize_UI):
        # Test if the function is called
        mock_customize_UI.return_value = True
        result = user_interface.customize_UI()
        self.assertTrue(result)
        mock_customize_UI.assert_called_once()

    @patch('src.user_interface.generate_report')
    def test_generate_report(self, mock_generate_report):
        # Test if the function is called
        mock_generate_report.return_value = True
        result = user_interface.generate_report()
        self.assertTrue(result)
        mock_generate_report.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```
import sys, os, unittest
from unittest.mock import patch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from Dec2Hex import decimal_to_hex, get_valid_integer, main


class Tests_Dec2Hex(unittest.TestCase):

    def test_decimal_to_hex_integer_input(self):
        self.assertEqual(decimal_to_hex(10), "A")
        self.assertEqual(decimal_to_hex(255), "FF")
        self.assertEqual(decimal_to_hex(42), "2A")

    def test_decimal_to_hex_negative_input(self):
        self.assertEqual(decimal_to_hex(-10), "-A")
        self.assertEqual(decimal_to_hex(-255), "-FF")
        self.assertEqual(decimal_to_hex(-42), "-2A")

    def test_decimal_to_hex_zero_input(self):
        self.assertEqual(decimal_to_hex(0), "0")

    def test_main_input_no_argument(self): 
        result = subprocess.run(
            [sys.executable, "src/Dec2Hex.py"],  
            capture_output=True,
            text=True
        )
        expected_message = "Error: No input argument provided.\nUsage: python script.py <decimal_number>"
        self.assertTrue(
            expected_message in result.stderr or expected_message in result.stdout,
            f"Expected '{expected_message}' but got '{result.stderr}'"
        )
   
    @patch('builtins.input', return_value='5')  
    def test_get_valid_integer_integer_input(self, mock_input):
        result = get_valid_integer()
        self.assertEqual(result, 5)  

    @patch('builtins.input', return_value='-10') 
    def test_get_valid_integer_negative_input(self, mock_input):
        result = get_valid_integer()
        self.assertEqual(result, -10)  

    @patch('builtins.input', return_value='0')  
    def test_get_valid_integer_zero_input(self, mock_input):
        result = get_valid_integer()
        self.assertEqual(result, 0)  

    @patch('builtins.input', side_effect=['c', '*', '10'])
    @patch('builtins.print')
    def test_get_valid_integer_invalid_then_valid_input(self, mock_print, mock_input):
        result = get_valid_integer()
        self.assertEqual(result, 10)
        mock_print.assert_any_call("Invalid input! Please provide a valid integer.")

    @patch('builtins.input', side_effect=[''])
    @patch('builtins.print')  
    def test_get_valid_integer_no_input(self, mock_print, mock_input):
        with self.assertRaises(SystemExit) as exc:
            get_valid_integer()
        self.assertEqual(exc.exception.code, 1)
        mock_print.assert_any_call("Error: No input argument provided.\nUsage: python script.py <decimal_number>")

if __name__ == '__main__':
    unittest.main()



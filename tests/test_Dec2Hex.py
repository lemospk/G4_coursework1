import subprocess
import sys, os, unittest
from unittest.mock import patch

# Adding the path to the 'src' directory to import the necessary functions from Dec2Hex
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from Dec2Hex import decimal_to_hex, get_valid_integer

class Test_Dec2Hex(unittest.TestCase):

    # Test to check the conversion of positive integers to hexadecimal on function decimal_to_hex
    def test_decimal_to_hex_integer_input(self):
        # Test conversion of 10 to hexadecimal, expected output is "A"
        self.assertEqual(decimal_to_hex(10), "A")
        # Test conversion of 255 to hexadecimal, expected output is "FF"
        self.assertEqual(decimal_to_hex(255), "FF")
        # Test conversion of 42 to hexadecimal, expected output is "2A"
        self.assertEqual(decimal_to_hex(42), "2A")

    # Test to check the conversion of negative integers to hexadecimal on function decimal_to_hex
    def test_decimal_to_hex_negative_input(self):
        # Test conversion of -10 to hexadecimal, expected output is "-A"
        self.assertEqual(decimal_to_hex(-10), "-A")
        # Test conversion of -255 to hexadecimal, expected output is "-FF"
        self.assertEqual(decimal_to_hex(-255), "-FF")
        # Test conversion of -42 to hexadecimal, expected output is "-2A"
        self.assertEqual(decimal_to_hex(-42), "-2A")

    # Test to check the conversion of zero to hexadecimal on function decimal_to_hex
    def test_decimal_to_hex_zero_input(self):
        # Test conversion of 0 to hexadecimal, expected output is "0"
        self.assertEqual(decimal_to_hex(0), "0")

    # Test to check the behavior of the script when no argument is provided in main
    def test_main_input_no_argument(self): 
        # Run the script with no arguments and capture the output
        result = subprocess.run(
            [sys.executable, "src/Dec2Hex.py"],  # Running the script
            capture_output=True,  # Capture stdout and stderr
            text=True  # Ensure the output is returned as text
        )
        # Define the expected error message when no input argument is given
        expected_message = "Error: No input argument provided.\nUsage: python script.py <decimal_number>"
        # Assert that the error message is in the output (stderr or stdout)
        self.assertTrue(
            expected_message in result.stderr or expected_message in result.stdout,
            f"Expected '{expected_message}' but got '{result.stderr}'"
        )

    # Test to check the behavior when the user inputs a valid integer on function get_valid_integer
    @patch('builtins.input', return_value='5')  
    def test_get_valid_integer_integer_input(self, mock_input):
        # Simulate user input of '5' for get_valid_integer() function
        result = get_valid_integer()
        # Assert that the returned value is 5
        self.assertEqual(result, 5)  

    # Test to check the behavior when the user inputs a negative integer on function get_valid_integer
    @patch('builtins.input', return_value='-10') 
    def test_get_valid_integer_negative_input(self, mock_input):
        # Simulate user input of '-10' for get_valid_integer() function
        result = get_valid_integer()
        # Assert that the returned value is -10
        self.assertEqual(result, -10)  

    # Test to check the behavior when the user inputs zero on function get_valid_integer
    @patch('builtins.input', return_value='0')  
    def test_get_valid_integer_zero_input(self, mock_input):
        # Simulate user input of '0' for get_valid_integer() function
        result = get_valid_integer()
        # Assert that the returned value is 0
        self.assertEqual(result, 0)  

    # Test to check the behavior of get_valid_integer function when the user inputs invalid values initially, followed by a valid integer
    @patch('builtins.input', side_effect=['c', '*', '10'])
    @patch('builtins.print')
    def test_get_valid_integer_invalid_then_valid_input(self, mock_print, mock_input):
        # Simulate invalid inputs ('c', '*') followed by a valid input ('10') for get_valid_integer()
        result = get_valid_integer()
        # Assert that the final valid input is returned (10)
        self.assertEqual(result, 10)
        # Check that the invalid input caused the print statement to be called with the appropriate error message
        mock_print.assert_any_call("Invalid input! Please provide a valid integer.")

    # Test to check the behavior when the user provides no input on function get_valid_integer
    @patch('builtins.input', side_effect=[''])
    @patch('builtins.print')  
    def test_get_valid_integer_no_input(self, mock_print, mock_input):
        # Simulate empty input for get_valid_integer()
        with self.assertRaises(SystemExit) as exc:
            get_valid_integer()
        # Assert that the script exits with status code 1 (error due to missing input)
        self.assertEqual(exc.exception.code, 1)
        # Check that the appropriate error message is printed
        mock_print.assert_any_call("Error: No input argument provided.\nUsage: python script.py <decimal_number>")

# Execute the tests if this script is executed directly
if __name__ == '__main__':
    unittest.main()
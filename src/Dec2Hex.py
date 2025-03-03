import sys

def decimal_to_hex(decimal_value):
    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hexadecimal = ""
    num = abs(decimal_value)

    if(decimal_value < 0):
        print(f"Converting the Decimal Value -{num} to Hex...")
    else:
        print(f"Converting the Decimal Value {num} to Hex...")

    if num == 0: # Add the rule that hexadecimal of zero is 0
        hexadecimal = "0"  
    else:
        while num != 0: 
            rem = num % 16
            hexadecimal = hex_chars[rem] + hexadecimal
            num //= 16

    if decimal_value < 0:  # Add negative sign back if the input was negative
        hexadecimal = "-" + hexadecimal

    if decimal_value == 0: 
        hexadecimal = "0"

    print(f"Hexadecimal representation is: {hexadecimal}")
    return hexadecimal # Return the hexadecimal value for testing

def get_valid_integer():
    print("Invalid input! Please provide a valid integer.")
    while True:
        user_input = input("Enter a integer: ")
        if not user_input:   # Return error for no input argument
            print("Error: No input argument provided.\nUsage: python script.py <decimal_number>")
            sys.exit(1)
        else:
            try:
                return int(user_input)
            except ValueError:
                print("Invalid input! Please provide a valid integer.")    


if __name__ == "__main__":
    if len(sys.argv) > 1: 
        try:
            decimal_value = int(sys.argv[1])
            decimal_to_hex(decimal_value)
        except ValueError:
            # Provide error handling for non-integer inputs      
            decimal_value = get_valid_integer()
            decimal_to_hex(decimal_value)
    else: # Return error for no input argument
        print("Error: No input argument provided.\nUsage: python script.py <decimal_number>")


# Define a custom exception by subclassing the Exception class
class NegativeValueError(Exception):
    # Constructor that takes an error message as input
    def __init__(self, message="Negative values are not allowed"):
        self.message = message
        super().__init__(self.message)

# Function that raises the custom exception
def process_positive_number(value):
    if value < 0:
        raise NegativeValueError(f"Invalid input: {value} is negative!")
    else:
        print(f"Processing the positive number: {value}")

# Test the function with positive and negative inputs
try:
    number = int(input("Enter a positive number: "))  # Get user input
    process_positive_number(number)  # Process the number
except NegativeValueError as e:
    print(f"Error: {e}")  # Handle the custom exception
except ValueError:
    print("Invalid input! Please enter an integer.")

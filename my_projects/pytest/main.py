import sys
import calculator_module

def select_operation() -> str | None:
    """Prompts the user to select an operation to perform."""
    retries = 0
    while retries < 3:
        option = input("Please select an option to continue: \
                        \n1. Increment a number by 1 \
                        \n2. Decrement a number by 1\n")
        if option not in ["1", "2"]:
            print("Invalid option. Please try again.")
            retries += 1
        else:
            return option
    return None

def select_integer() -> int | None:
    """Prompts the user to enter an integer."""
    retries = 0
    while retries < 3:
        try:
            result = int(input("Please enter a number: "))
            return result
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        retries += 1
    return None

def perform_calculation(operation: str, number: int) -> int:
    """Performs the selected calculation and displays the result."""
    operations = {
            "1": "increment_by_one",
            "2": "decrement_by_one"
        }
    
    result = getattr(calculator_module, operations[operation])(number)
    return result

def print_the_result(operation: str, result: int) -> None:
    """Prints a message indicating the result of the operation."""
    operations = {
        "1": "incremented",
        "2": "decremented"
    }
    print(f"The {operations[operation]} value is: {result}")


print("Hi, this is a calculator program. I can increment and decrement numbers by 1.")
operation = select_operation()
if operation is None:
    print("No valid operation selected. Exiting the program.")
    sys.exit(1)
    
integer = select_integer()
if integer is None:
    print("No valid number entered. Exiting the program.")
    sys.exit(1)

result = perform_calculation(operation, integer)
print_the_result(operation, result)

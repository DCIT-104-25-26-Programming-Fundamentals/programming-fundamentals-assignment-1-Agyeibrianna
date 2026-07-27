# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in

def add(a, b):
    """Return the sum of a and b."""
    return a + b
 
 
def subtract(a, b):
    """Return the difference of a and b."""
    return a - b
 
 
def multiply(a, b):
    """Return the product of a and b."""
    return a * b
 
 
def divide(a, b):
    """
    Return a divided by b, rounded to 2 decimal places.
    Returns None if b is zero.
    """
    if b == 0:
        return None
    return round(a / b, 2)
 
 
def modulus(a, b):
    """
    Return the remainder of a divided by b.
    Returns None if b is zero.
    """
    if b == 0:
        return None
    return a % b
 
 
def exponentiate(a, b):
    """Return a raised to the power of b."""
    return a ** b
 
 
def print_menu():
    """
    Display the calculator menu.
    """
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")
 
 
def get_operands():
    """
    Prompt the user for two numbers and return them as floats.
    """
    first = float(input("Enter first number : "))
    second = float(input("Enter second number: "))
    return first, second
 
 
def main():
    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
        "5": ("%", modulus),
        "6": ("**", exponentiate),
    }
 
    while True:
        print_menu()
        choice = input("Select an operation (1-7): ")
 
        if choice == "7":
            print("Goodbye!")
            break
 
        if choice not in operations:
            print("Error: Invalid choice. Please enter a number from 1 to 7.")
            continue
 
        symbol, operation = operations[choice]
        first, second = get_operands()
 
        if choice in ("4", "5") and second == 0:
            print("Error: Cannot divide by zero.")
            continue
 
        result = operation(first, second)
        print(f"Result: {first:g} {symbol} {second:g} = {result:g}")
 
 
if __name__ == "__main__":
    main()
 


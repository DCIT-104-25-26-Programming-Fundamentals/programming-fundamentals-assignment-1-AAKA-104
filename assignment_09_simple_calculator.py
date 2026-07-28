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
# =============================================================================

def display_menu():
    """Display the calculator menu options."""
    print("\n" + "=" * 30)
    print("     SIMPLE CALCULATOR")
    print("=" * 30)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def get_numbers():
    """Get two numbers from the user."""
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2


def addition(num1, num2):
    """Return the sum of two numbers."""
    return num1 + num2


def subtraction(num1, num2):
    """Return the difference of two numbers."""
    return num1 - num2


def multiplication(num1, num2):
    """Return the product of two numbers."""
    return num1 * num2


def division(num1, num2):
    """Return the quotient of two numbers."""
    if num2 == 0:
        return None
    return num1 / num2


def modulus(num1, num2):
    """Return the remainder of two numbers."""
    if num2 == 0:
        return None
    return num1 % num2


def exponentiation(num1, num2):
    """Return num1 raised to the power of num2."""
    return num1 ** num2


def main():
    """Main program loop."""
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ")
        
        if choice == "7":
            print("Goodbye!")
            break
        
        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice. Please enter a number between 1 and 7.")
            continue
        
        num1, num2 = get_numbers()
        
        if choice == "1":
            result = addition(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        
        elif choice == "2":
            result = subtraction(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        
        elif choice == "3":
            result = multiplication(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        
        elif choice == "4":
            result = division(num1, num2)
            if result is None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {num1} / {num2} = {result:.2f}")
        
        elif choice == "5":
            result = modulus(num1, num2)
            if result is None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {num1} % {num2} = {result}")
        
        elif choice == "6":
            result = exponentiation(num1, num2)
            print(f"Result: {num1} ** {num2} = {result}")


if __name__ == "__main__":
    main()
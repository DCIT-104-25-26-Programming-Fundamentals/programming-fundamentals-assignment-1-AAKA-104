# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def print_fibonacci_sequence(n):
    """Part A: Print the first N terms of the Fibonacci sequence."""
    if n <= 0:
        print("Error: Number of terms must be positive.")
        return
    
    # Handle the first two terms separately
    if n == 1:
        print("Fibonacci sequence: 0")
        return
    
    # Start with the first two terms
    a = 0
    b = 1
    
    # Build the sequence string
    sequence = "0 1"
    
    # Generate remaining terms
    for i in range(2, n):
        next_term = a + b
        sequence += f" {next_term}"
        a = b
        b = next_term
    
    print(f"Fibonacci sequence: {sequence}")


def is_fibonacci_number(num):
    """Part B: Check if a number belongs to the Fibonacci sequence."""
    if num < 0:
        return False
    
    # Generate Fibonacci numbers until we reach or exceed the target
    a = 0
    b = 1
    
    # Check if the number is 0 or 1 (first two Fibonacci numbers)
    if num == 0 or num == 1:
        return True
    
    # Generate terms until we reach or pass the target
    while b < num:
        next_term = a + b
        a = b
        b = next_term
    
    # If b equals the target, it's a Fibonacci number
    return b == num


def main():
    print("=" * 50)
    print("PART A: Print First N Terms")
    print("=" * 50)
    
    try:
        n = int(input("How many terms? "))
        print_fibonacci_sequence(n)
    except ValueError:
        print("Error: Please enter a valid integer.")
    
    print("\n" + "=" * 50)
    print("PART B: Check if Number is Fibonacci")
    print("=" * 50)
    
    try:
        num = int(input("Enter a number to check: "))
        if is_fibonacci_number(num):
            print(f"{num} is a Fibonacci number.")
        else:
            print(f"{num} is NOT a Fibonacci number.")
    except ValueError:
        print("Error: Please enter a valid integer.")


if __name__ == "__main__":
    main()


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

def generate_fibonacci_terms(n):
    """
    Return a list containing the first `n` terms of the Fibonacci sequence,
    generated using a loop.
    """
    sequence = []
    a, b = 0, 1
 
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
 
    return sequence
 
 
def is_fibonacci_number(number):
    """
    Return True if `number` appears in the Fibonacci sequence, False otherwise.
    Uses a loop to generate terms up to `number`.
    """
    if number < 0:
        return False
 
    a, b = 0, 1
 
    while a <= number:
        if a == number:
            return True
        a, b = b, a + b
 
    return False
 
 
def run_print_terms():
    print("\n--- PART A: Print the First N Terms ---")
    n = int(input("How many terms? "))
 
    if n <= 0:
        print("Error: N must be a positive integer.")
        return
 
    terms = generate_fibonacci_terms(n)
    terms_str = " ".join(str(term) for term in terms)
    print(f"Fibonacci sequence: {terms_str}")
 
 
def run_check_membership():
    print("\n--- PART B: Check if a Number Belongs to the Sequence ---")
    number = int(input("Enter a number to check: "))
 
    if is_fibonacci_number(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")
 
 
def main():
    run_print_terms()
    run_check_membership()
 
 
if __name__ == "__main__":
    main()


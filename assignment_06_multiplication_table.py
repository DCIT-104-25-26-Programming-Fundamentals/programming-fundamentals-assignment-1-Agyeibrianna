# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in

def print_table(number):
    """
    Print the multiplication table for `number` from 1 to 12.
    """
    print(f"Multiplication Table for {number}:")
    for multiplier in range(1, 13):
        product = number * multiplier
        print(f"{number}  x  {multiplier:<2} =  {product}")
 
 
def print_tables_up_to(n):
    """
    Print the full multiplication table for every number from 1 to n,
    separated by a divider line.
    """
    for number in range(1, n + 1):
        print_table(number)
        if number != n:
            print("-" * 29)
 
 
def main():
    single_input = input("Enter a number for its multiplication table: ")
    number = int(single_input)
    print()
    print_table(number)
 
    print()
    n_input = input("Enter N to print tables from 1 to N: ")
    n = int(n_input)
 
    if n <= 0:
        print("Error: N must be a positive integer.")
        return
 
    print()
    print_tables_up_to(n)
 
 
if __name__ == "__main__":
    main()


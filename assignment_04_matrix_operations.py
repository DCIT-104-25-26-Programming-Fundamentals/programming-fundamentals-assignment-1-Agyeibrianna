# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in

def read_matrix(name="Matrix", rows=None, cols=None):
    """
    Read a matrix from the user as a list of lists of numbers.
    If rows/cols are not provided, the user is prompted for them.
    """
    if rows is None:
        rows = int(input(f"Enter number of rows for {name}: "))
    if cols is None:
        cols = int(input(f"Enter number of columns for {name}: "))
 
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i + 1}: ").split()
            if len(row_input) != cols:
                print(f"Error: expected {cols} values, got {len(row_input)}. Try again.")
                continue
            row = [float(value) for value in row_input]
            matrix.append(row)
            break
 
    return matrix
 
 
def print_matrix(matrix, title="Matrix"):
    """
    Display a matrix in a neat, aligned grid format.
    """
    print(f"\n{title}:")
    for row in matrix:
        formatted_row = "  ".join(f"{value:g}" for value in row)
        print(formatted_row)
 
 
def transpose_matrix(matrix):
    """
    Return the transpose of `matrix` using nested loops.
    """
    rows = len(matrix)
    cols = len(matrix[0])
 
    transposed = [[0] * rows for _ in range(cols)]
 
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
 
    return transposed
 
 
def add_matrices(matrix_a, matrix_b):
    """
    Return the element-wise sum of two same-sized matrices using nested loops.
    """
    rows = len(matrix_a)
    cols = len(matrix_a[0])
 
    result = [[0] * cols for _ in range(rows)]
 
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
 
    return result
 
 
def multiply_matrices(matrix_a, matrix_b):
    """
    Return the matrix product of A (M x N) and B (N x P) using nested loops.
    """
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
 
    result = [[0] * cols_b for _ in range(rows_a)]
 
    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total
 
    return result
 
 
def run_transpose():
    print("\n--- PART A: Transpose a Matrix ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix("Matrix", rows, cols)
 
    print_matrix(matrix, "Original Matrix")
    transposed = transpose_matrix(matrix)
    print_matrix(transposed, "Transposed Matrix")
 
 
def run_addition():
    print("\n--- PART B: Add Two Matrices ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
 
    print("\nEnter values for Matrix A:")
    matrix_a = read_matrix("Matrix A", rows, cols)
 
    print("\nEnter values for Matrix B:")
    matrix_b = read_matrix("Matrix B", rows, cols)
 
    print_matrix(matrix_a, "Matrix A")
    print_matrix(matrix_b, "Matrix B")
 
    result = add_matrices(matrix_a, matrix_b)
    print_matrix(result, "Sum (A + B)")
 
 
def run_multiplication():
    print("\n--- PART C: Multiply Two Matrices ---")
    m = int(input("Enter number of rows for Matrix A: "))
    n = int(input("Enter number of columns for Matrix A (= rows for Matrix B): "))
    p = int(input("Enter number of columns for Matrix B: "))
 
    print("\nEnter values for Matrix A:")
    matrix_a = read_matrix("Matrix A", m, n)
 
    print("\nEnter values for Matrix B:")
    matrix_b = read_matrix("Matrix B", n, p)
 
    print_matrix(matrix_a, "Matrix A")
    print_matrix(matrix_b, "Matrix B")
 
    result = multiply_matrices(matrix_a, matrix_b)
    print_matrix(result, "Product (A x B)")
 
 
def main():
    print("Matrix Operations")
    print("1. Transpose a Matrix")
    print("2. Add Two Matrices")
    print("3. Multiply Two Matrices")
 
    choice = input("Choose an operation (1-3): ").strip()
 
    if choice == "1":
        run_transpose()
    elif choice == "2":
        run_addition()
    elif choice == "3":
        run_multiplication()
    else:
        print("Error: Invalid choice. Please enter 1, 2, or 3.")
 
 
if __name__ == "__main__":
    main()

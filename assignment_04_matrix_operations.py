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
# =============================================================================

def read_matrix(rows, cols):
    """Read a matrix from user input."""
    matrix = []
    for i in range(rows):
        row_input = input(f"Enter row {i+1}: ")
        # Split the input by spaces and convert each to integer
        row = [int(num) for num in row_input.split()]
        matrix.append(row)
    return matrix


def display_matrix(matrix):
    """Display a matrix in a neat grid format."""
    for row in matrix:
        # Format each number to be right-aligned in 5 spaces
        formatted_row = " ".join(f"{num:5}" for num in row)
        print(formatted_row)


def transpose_matrix(matrix):
    """Part A: Return the transpose of a matrix."""
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create a new matrix with cols rows and rows columns
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    
    return transposed


def add_matrices(matrix_a, matrix_b):
    """Part B: Return the element-wise sum of two matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)
    
    return result


def multiply_matrices(matrix_a, matrix_b):
    """Part C: Return the product of two matrices."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])
    
    # Initialize result matrix with zeros
    result = []
    for i in range(rows_a):
        new_row = [0] * cols_b
        result.append(new_row)
    
    # Matrix multiplication: result[i][j] = sum of A[i][k] * B[k][j]
    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):  # or rows_b (they must be equal)
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total
    
    return result


def main():
    print("=" * 50)
    print("PART A: Transpose a Matrix")
    print("=" * 50)
    
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    print("\nEnter the matrix:")
    matrix = read_matrix(rows, cols)
    
    print("\nOriginal Matrix:")
    display_matrix(matrix)
    
    transposed = transpose_matrix(matrix)
    print("\nTransposed Matrix:")
    display_matrix(transposed)
    
    print("\n" + "=" * 50)
    print("PART B: Add Two Matrices")
    print("=" * 50)
    
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    print("\nEnter first matrix:")
    matrix_a = read_matrix(rows, cols)
    
    print("\nEnter second matrix:")
    matrix_b = read_matrix(rows, cols)
    
    print("\nMatrix A:")
    display_matrix(matrix_a)
    print("\nMatrix B:")
    display_matrix(matrix_b)
    
    sum_matrix = add_matrices(matrix_a, matrix_b)
    print("\nA + B:")
    display_matrix(sum_matrix)
    
    print("\n" + "=" * 50)
    print("PART C: Multiply Two Matrices")
    print("=" * 50)
    
    rows_a = int(input("Enter rows for matrix A: "))
    cols_a = int(input("Enter columns for matrix A: "))
    
    print("\nEnter matrix A:")
    matrix_a = read_matrix(rows_a, cols_a)
    
    rows_b = int(input("\nEnter rows for matrix B: "))
    cols_b = int(input("Enter columns for matrix B: "))
    
    # Check if multiplication is possible
    if cols_a != rows_b:
        print("\nError: Cannot multiply matrices!")
        print(f"Matrix A has {cols_a} columns but Matrix B has {rows_b} rows.")
        print("For multiplication, columns of A must equal rows of B.")
        return
    
    print("\nEnter matrix B:")
    matrix_b = read_matrix(rows_b, cols_b)
    
    print("\nMatrix A:")
    display_matrix(matrix_a)
    print("\nMatrix B:")
    display_matrix(matrix_b)
    
    product = multiply_matrices(matrix_a, matrix_b)
    print("\nA × B:")
    display_matrix(product)


if __name__ == "__main__":
    main()

#interactive matrix operation calculator 
import numpy as np
def get_matrix(name):
    rows = int(input(f"Enter number of rows for Matrix {name}: "))
    cols = int(input(f"Enter number of columns for Matrix {name}: "))
    print("don't use comma instead use space")
    print(f"Enter elements for Matrix {name} row by row:")
    elements = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        elements.append(row)
    return np.array(elements)

# Get user matrices
print("Matrix A")
A = get_matrix('A')

print("\nMatrix B")
B = get_matrix('B')

# Menu
print("\nChoose an operation:")
print("1. Addition (A + B)")
print("2. Subtraction (A - B)")
print("3. Multiplication (A * B)")
print("4. Inverse (only for Matrix A)")
print("5. Transpose (Matrix A and B)")

choice = input("Enter your choice (1-5): ")

# Perform operation
if choice == '1':
    if A.shape == B.shape:
        print("\nResult of A + B:\n", A + B)
    else:
        print("Error: Matrices must have the same dimensions for addition.")
elif choice == '2':
    if A.shape == B.shape:
        print("\nResult of A - B:\n", A - B)
    else:
        print("Error: Matrices must have the same dimensions for subtraction.")
elif choice == '3':
    if A.shape[1] == B.shape[0]:
        print("\nResult of A * B:\n", np.dot(A, B))
    else:
        print("Error: Columns of A must match rows of B for multiplication.")
elif choice == '4':
    if A.shape[0] == A.shape[1]:
        try:
            print("\nInverse of Matrix A:\n", np.linalg.inv(A))
        except np.linalg.LinAlgError:
            print("Matrix A is not invertible.")
    else:
        print("Error: Matrix A must be square for inversion.")
elif choice == '5':
    print("\nTranspose of Matrix A:\n", A.T)
    print("Transpose of Matrix B:\n", B.T)
else:
    print("Invalid choice.")


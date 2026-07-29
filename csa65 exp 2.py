import numpy as np

# Sales data matrices
A = np.array([[10, 20],
              [30, 40]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix Addition
print("\nAddition (A + B):")
print(A + B)

# Matrix Subtraction
print("\nSubtraction (A - B):")
print(A - B)

# Matrix Multiplication
print("\nMultiplication (A x B):")
print(np.matmul(A, B))

# Matrix Transpose
print("\nTranspose of Matrix A:")
print(A.T)

# Matrix Inverse
print("\nInverse of Matrix A:")
print(np.linalg.inv(A))
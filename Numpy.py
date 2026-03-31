Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import numpy as np
# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5, 6])


print("Original Array:")
Original Array:
print(arr)
[1 2 3 4 5 6]

# Reshape the array (2 rows, 3 columns)
reshaped_arr = arr.reshape(2, 3)
print("\nReshaped Array (2x3):")

Reshaped Array (2x3):
print(reshaped_arr)
[[1 2 3]
 [4 5 6]]
# Indexing (access element at row 1, column 2)
print("\nElement at position [1][2]:", reshaped_arr[1][2])


Element at position [1][2]: 6
# Calculate sum of all elements
total_sum = np.sum(arr)
print("\nSum of all elements:", total_sum)


Sum of all elements: 21

import numpy as np
# Create two matrices
A = np.array([[1, 2],[3, 4]])
B = np.array([[5, 6],[7, 8]])
print("Matrix A:")
Matrix A:
>>> print(A)
[[1 2]
 [3 4]]
>>> print("\nMatrix B:")

Matrix B:
>>> print(B)
[[5 6]
 [7 8]]
>>> # Matrix Addition
... addition = A + B
... print("\nAddition (A + B):")
SyntaxError: multiple statements found while compiling a single statement
>>> # Matrix Addition
... addition = A + B
>>> print("\nAddition (A + B):")

Addition (A + B):
>>> print(addition)
[[ 6  8]
 [10 12]]
>>> 
... # Matrix Multiplication
... multiplication = np.dot(A, B)
>>> print("\nMultiplication (A * B):")

Multiplication (A * B):
>>> print(multiplication)
[[19 22]
 [43 50]]
>>> # Transpose of Matrix A
... transpose = A.T
>>> print("\nTranspose of Matrix A:")

Transpose of Matrix A:
>>> print(transpose)
[[1 3]
 [2 4]]

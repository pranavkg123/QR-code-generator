import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Element-wise operations
print("Addition:", arr1 + arr2)
print("Multiplication:", arr1 * arr2)

# Scalar operations
print("Scalar Multiplication:", arr1 * 2)

# Matrix operations
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
print("Matrix Multiplication:", np.dot(matrix1, matrix2))

# Other operations
print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Max:", np.max(arr1))

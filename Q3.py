#Q.3)
import numpy as np
# 4x5 matrix of random integers between 20 and 80
matrix = np.random.randint(20, 81, size=(4, 5))
print("Matrix:")
print(matrix)
#operations for the entire matrix
print("\nMinimum Value:", matrix.min())
print("Maximum Value:", matrix.max())
print("Sum of All Elements:", matrix.sum())
print("Mean:", matrix.mean())
print("Standard Deviation:", matrix.std())
# Sum of each row
print("\nRow-wise Sum:")
print(matrix.sum(axis=1))
# Sum of each column
print("\nColumn-wise Sum:")
print(matrix.sum(axis=0))

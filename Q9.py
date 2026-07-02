#Q.9)
import numpy as np
arr = np.random.randn(6, 6)
print("Original Matrix:")
print(arr)
print("\nShape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
# Index of the maximum value
max_index = np.unravel_index(np.argmax(arr), arr.shape)
print("\nIndex of Maximum Value:", max_index)
# Index of the minimum value
min_index = np.unravel_index(np.argmin(arr), arr.shape)
print("Index of Minimum Value:", min_index)
# Top-left 3x3 submatrix
print("\nTop-Left 3x3 Submatrix:")
print(arr[:3, :3])
# Replacing all negative numbers with their absolute value
arr[arr < 0] = np.abs(arr[arr < 0])
print("\nModified Matrix:")
print(arr)
print("\nMean of Modified Matrix:", arr.mean())

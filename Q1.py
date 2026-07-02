#Q.1)
import numpy as np
# 2D array of shape (5, 6) with random integers between 10 and 100
arr = np.random.randint(10, 101, size=(5, 6))
print("Array:")
print(arr)
# array properties
print("\nShape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)

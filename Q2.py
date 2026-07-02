#Q.2)
import numpy as np
# 1D array of 20 random numbers between 1 and 50
arr = np.random.randint(1, 51, 20)
print("Array:")
print(arr)
# Minimum value and its index
print("\nMinimum Value:", arr.min())
print("Index of Minimum Value:", arr.argmin())
# Maximum value and its index
print("\nMaximum Value:", arr.max())
print("Index of Maximum Value:", arr.argmax())
# Sum of all elements
print("\nSum:", arr.sum())
# Mean and Standard Deviation
print("Mean:", arr.mean())
print("Standard Deviation:", arr.std())
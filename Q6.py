#Q.6)
import numpy as np
# matrix of random integers between 1 and 100
arr = np.random.randint(1, 101, size=(5, 5))
print("Original Array:")
print(arr)
#diagonal elements
print("\nDiagonal Elements:")
print(np.diag(arr))
#elements greater than 50
print("\nElements Greater Than 50:")
print(arr[arr > 50])
# Replace all elements less than 30 with 0
arr[arr < 30] = 0
print("\nModified Array:")
print(arr)

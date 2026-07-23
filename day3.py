import numpy as np

print("========== NumPy Basics ==========\n")

# Creating Arrays
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("1D Array:")
print(arr1)

print("\n2D Array:")
print(arr2)

# Array Information
print("\nShape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Data Type:", arr2.dtype)

# Indexing
print("\nFirst Element:", arr1[0])
print("Last Element:", arr1[-1])
print("Element at Row 2, Column 3:", arr2[1][2])

# Slicing
print("\nFirst Three Elements:", arr1[:3])

# Mathematical Operations
print("\nAddition:")
print(arr1 + 5)

print("\nMultiplication:")
print(arr1 * 2)

print("\nSquare:")
print(arr1 ** 2)

# Statistics
print("\nSum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Maximum:", np.max(arr1))
print("Minimum:", np.min(arr1))

# Random Array
random_array = np.random.randint(1, 100, size=(3,3))

print("\nRandom 3x3 Array:")
print(random_array)

print("\nProgram Completed Successfully!")
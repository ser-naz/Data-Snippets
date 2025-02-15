import numpy as np
import pandas as pd

# **********************************************************************************************************************
# NumPy Cheat Sheet
# **********************************************************************************************************************

# Creating NumPy 1D Arrays
arr1 = np.array([1, 2, 3, 4, 5])  # Creating a 1D array
print(arr1)
# Output: [1 2 3 4 5] type - int64 (or int32 depending on system)
print(arr1.shape)  # Returns (rows, columns) a tuple representing the array’s dimensions
# Output: (5,)

print(arr1.dtype)
# Output: int64

# **********************************************************************************************************************

# Converting an array to list
arr_l = arr1.tolist()
print(arr_l)
# Output: [1, 2, 3, 4, 5] - type list

# **********************************************************************************************************************

# Reshaping one dimensional array into 2D
arr1D = np.array([1, 2, 3, 4, 5])

# Convert to a COLUMN vector (5 rows, 1 column)
arr2D_col = arr1D.reshape(-1, 1)
print(arr2D_col.shape)
print(arr2D_col)
# Output:
# (5, 1)

# [[1]
#  [2]
#  [3]
#  [4]
#  [5]]

# Convert to a ROW vector (1 row, 5 columns)
arr2D_row = arr1D.reshape(1, -1)
print(arr2D_row.shape)
print(arr2D_row)
# Output:
# (1, 5)

# [[1 2 3 4 5]]

# **********************************************************************************************************************

# Creating NumPy 2D Arrays
arr2 = np.array([[1, 2, 3], [4, 5, 6]])  # Creating a 2D array
print(arr2)
# Output:
# [[1 2 3]
#  [4 5 6]]

# Checking Array Shape, Size, and Data Type
print(arr2.shape)  # Returns (rows, columns) a tuple representing the array’s dimensions
# Output: (2, 3)

print(arr2.size)  # Total number of elements
# Output: 6

print(arr2.dtype)  # Data type of elements
# Output: int64 (or int32 depending on system)

# **********************************************************************************************************************

# Reshaping Arrays
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_2x3 = arr.reshape((2, 3))  # Reshaping to 2 rows, 3 columns
print(reshaped_2x3)
# Output:
# [[1 2 3]
#  [4 5 6]]

# Converts multi-dimensional array to 1D
flattened = reshaped_2x3.flatten()
print(flattened)
# Output: [1 2 3 4 5 6]

# **********************************************************************************************************************

# Creating Special Arrays
zeros_arr = np.zeros((3, 3))  # 3x3 array of zeros
print(zeros_arr)
# Output:
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

ones_arr = np.ones((2, 2))  # 2x2 array of ones
print(ones_arr)
# Output:
# [[1. 1.]
#  [1. 1.]]

identity_matrix = np.eye(3)  # 3x3 Identity matrix
print(identity_matrix)
# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# Creating array with random values
random_arr = np.random.rand(2, 3)  # 2x3 array with random values between 0 and 1
print(random_arr)
# Output: (random values, for example)
# [[0.72463475 0.88910385 0.55397289]
#  [0.53358625 0.20176248 0.11931758]]

# Random values between 1 and 100
random_arr_100 = 1 + (100 - 1) * np.random.rand(3, 5)
print(random_arr_100)
# Output:
# [[ 29.1852394   74.40460419  58.84535885  47.19480516  51.67938496]
#  [ 19.18938465  12.92847434  52.74141834  78.32197857  17.7616722 ]
#  [ 37.91777173  58.18805885  96.2744066   89.07684991  45.97579984]]

# **********************************************************************************************************************

# np.linspace(start, stop, num) generates an array with `num` evenly spaced values from `start` to `stop`, inclusive.
# Example: np.linspace(0, 10, 5) → [0.   2.5  5.   7.5 10.]
# Spacing between consecutive values: (stop - start) / (num - 1)
# For np.linspace(0, 10, 5), spacing = (10 - 0) / (5 - 1) = 2.5.
# start: The starting value of the array (0 in this case).
# stop: The ending value of the array (1 in this case).
# num: The number of evenly spaced values to generate (5 in this case).

linspace_arr = np.linspace(0, 10, 5)

print(linspace_arr)
# Output: [ 0.   2.5  5.   7.5 10. ]


# This generates 10 equally spaced values from 0 to 100, including both endpoints.
# The spacing between consecutive values is (100 - 0) / (10 - 1) = 11.11.
linspace_arr_100 = np.linspace(0, 100, 10)
print(linspace_arr_100)
# Output:  [ 0.    11.11  22.22  33.33  44.44  55.56  66.67  77.78  88.89 100. ]

# **********************************************************************************************************************

# Indexing and Slicing
arr = np.array([10, 20, 30, 40, 50])
print(arr[2])  # Accessing element at index 2
# Output: 30

print(arr[1:4])  # Slicing elements from index 1 to 3
# Output: [20 30 40]

arr2D_small = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
print(arr2D_small[1, 2])  # Accessing row 1, column 2
# Output: 6

# Slicing a 2D array
# arr2D[start_row:end_row, start_col:end_col]:
# This slices the array to include rows from start_row to end_row and columns from start_col to end_col.
arr2D = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20]])

# Slice the first two rows and first three columns
slice_1 = arr2D[:2, :3]
print(slice_1)
# Output:
# [[1 2 3]
#  [6 7 8]]

# Slice from the second row to the last row, and from the second column to the last column
slice_2 = arr2D[1:, 1:]
print(slice_2)
# Output:
# [[ 7  8  9 10]
#  [12 13 14 15]
#  [17 18 19 20]]

# Slice the first three rows and the last two columns
slice_3 = arr2D[:3, -2:]
print(slice_3)
# Output:
# [[ 4  5]
#  [ 9 10]
#  [14 15]]

# Slice the entire array except the last row and last column
slice_4 = arr2D[:-1, :-1]
print(slice_4)
# Output:
# [[ 1  2  3  4]
#  [ 6  7  8  9]
#  [11 12 13 14]]

# Slice only the middle two rows and middle three columns
slice_5 = arr2D[1:3, 1:4]
print(slice_5)
# Output:
# [[ 7  8  9]
#  [12 13 14]]

# **********************************************************************************************************************

# Mathematical Operations
arr_math = np.array([1, 2, 3, 4])

# Add 10 to each element
print(arr_math + 10)
# Output: [11 12 13 14]

# Multiply each element by 2
print(arr_math * 2)
# Output: [2 4 6 8]

# Square root of each element
print(np.sqrt(arr_math))
# Output: [1.         1.41421356 1.73205081 2.        ]

# Raising each element to the second power (square)
print(arr_math ** 2)  # Using the ** operator
print(np.power(arr_math, 2))  # Using np.power()
# Output: [ 1  4  9 16]

# **********************************************************************************************************************

# Aggregation Functions
arr_agg = np.array([5, 10, 15, 20])

# Sum of all elements
print(np.sum(arr_agg))
# Output: 50

# Mean (average)
print(np.mean(arr_agg))
# Output: 12.5

# Maximum value
print(np.max(arr_agg))
# Output: 20

# Minimum value
print(np.min(arr_agg))
# Output: 5

# Standard deviation
print(np.std(arr_agg))
# Output: 5.5901699437494745

# **********************************************************************************************************************

# Boolean Masking and Filtering
data = np.array([10, 15, 20, 25, 30])
mask = data > 15  # Create a boolean mask
filtered_data = data[mask]  # Apply mask to filter elements
print(filtered_data)
# Output: [20 25 30]   return one dimensional array

# Boolean mask to a 2D array, it returns a 1D array with only the elements that meet the condition,
# flattened into a single dimension. The result is essentially a 1D array of the filtered values.
data_2D = np.array([[10, 15, 20],
                    [25, 30, 35],
                    [40, 45, 50]])

mask = data_2D > 20  # Create a boolean mask (True where element > 20)

# Apply the mask to filter elements
filtered_data_2D = data_2D[mask] # or data_2D[data_2D > 20]

print(filtered_data_2D)
# Output: [25 30 35 40 45 50]   return one dimensional array

# **********************************************************************************************************************

# Stacking and Concatenation
# The position of the arrays affects the order in which they are placed,
# but the stacking operation itself works the same way regardless of their positions.

arrA = np.array([1, 2, 3])
arrB = np.array([4, 5, 6])
stacked_v = np.vstack((arrA, arrB))  # Vertical stacking
print(stacked_v)
# Output:
# [[1 2 3]
#  [4 5 6]]

stacked_h = np.hstack((arrA, arrB))  # Horizontal stacking
print(stacked_h)
# Output: [1 2 3 4 5 6]


# Different LENGTHS
# Different LENGTHS - Horizontal stacking
arrA = np.array([1, 2, 3])
arrB = np.array([4, 5, 6, 7])

stacked_h = np.hstack((arrA, arrB))  # Horizontal stacking
print(stacked_h)
# Output: [1 2 3 4 5 6 7]

# Different length - Vertical stacking will raise an error because the arrays have different lengths
arrA = np.array([1, 2, 3])
arrB = np.array([4, 5])

stacked_v = np.vstack((arrA, arrB))  # Vertical stacking
# This will raise an error because the arrays have different lengths.


# Stacking with 2D Arrays
# Vertical Stacking with 2D Arrays - must have the same number of columns
arrA = np.array([[1, 2], [3, 4]])  # 2x2 array
arrB = np.array([[5, 6], [7, 8]])  # 2x2 array

stacked_vert = np.vstack((arrA, arrB))  # Vertical stacking 2D Arrays
print(stacked_vert)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# Horizontal Stacking with 2D Arrays - must have the same number of rows
arrA = np.array([[1, 2], [3, 4]])  # 2x2 array
arrB = np.array([[5, 6], [7, 8]])  # 2x2 array

stacked_h = np.hstack((arrA, arrB))  # Horizontal stacking 2D Arrays
print(stacked_h)
# Output:
# [[1 2 5 6]
#  [3 4 7 8]]

# **********************************************************************************************************************

# Linear Algebra Operations
# matrix multiplication and inversion are widely used in machine learning
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Matrix multiplication
# The result of multiplying matrix1 and matrix2 is a new matrix where each element is calculated as
# the dot product of the rows of matrix1 with the columns of matrix2.
matrix_product = np.dot(matrix1, matrix2)
print(matrix_product)
# Output:
# [[19 22]
#  [43 50]]

# Inverse of a matrix
# The inverse of a matrix is a matrix such that when it is multiplied by the original matrix,
# the result is the identity matrix.
matrix_inv = np.linalg.inv(matrix1)
print(matrix_inv)
# Output:
# [[-2.   1. ]
#  [ 1.5 -0.5]]

# **********************************************************************************************************************

# Random Seeding for Reproducibility - widely used in machine learning
# Seeding allows you to control randomness and get consistent results across different runs of the code
# With the seed (np.random.seed(42)): No matter how many times you run the code, the output will always be the same.
# The number 42 is often used as a convention or a "default seed" in programming
# can be any number but to ensure the same sequence of random numbers each time you run the code with that SAME seed
np.random.seed(42)
random_numbers = np.random.rand(3)
print(random_numbers)
# Output (always the same when seed is set): [0.3745 0.9507 0.7319]

# **********************************************************************************************************************

# Handling NaN and Inf Values
data_nan = np.array([1, 2, np.nan, 4, 5])
nan_mask = np.isnan(data_nan) # [False False  True False False]
cleaned_data = data_nan[~nan_mask]  # Remove NaN values
print(cleaned_data)
# Output:
# [1. 2. 4. 5.]

# **********************************************************************************************************************

# Sorting Arrays
arr_sort = np.array([3, 1, 5, 2, 4])
sorted_arr = np.sort(arr_sort)
print(sorted_arr)
# Output: [1 2 3 4 5]

# **********************************************************************************************************************

# Mixed array - numbers and letters in a numpy array

# Create an array with both numbers and letters (strings)
mixed_array = np.array([1, 2, 'a', 4, 'b'], dtype=object)
print(mixed_array)
# Output:
# [1 2 'a' 4 'b'] type - object

# perform operations on a mixed array
result = mixed_array + 1  # Adds 1 to the numeric elements
print(result)
# Output:
# [2 3 'a' 5 'b'] type - object

# Create a numpy array with letters (strings)
letters_array = np.array(['a', 'b', 'c', 'd', 'e'], dtype=object)
print(letters_array)
# Output:
# ['a' 'b' 'c' 'd' 'e'] type - object

letters_with_none = np.array(['a', 'b', None, 'd'], dtype=object)
print(letters_with_none)
# Output:
# ['a' 'b' None 'd'] type - object


# Dates and Time
# Create an array of dates
date_array = np.array(['2023-01-01', '2023-01-02', '2023-01-03'], dtype='datetime64[D]')
print(date_array)
# Output:
# ['2023-01-01' '2023-01-02' '2023-01-03'] type - datetime64[D]


# Performing Date Arithmetic
# Adding 5 days to each date
new_dates = date_array + np.timedelta64(5, 'D')
print(new_dates)
# Output:
# ['2023-01-06' '2023-01-07' '2023-01-08']

# Difference between two dates
diff = date_array[2] - date_array[0]
print(diff)
# Output:
# 2 days

# **********************************************************************************************************************

# np.where() function is useful for conditional element selection and replacement
arr_wh = np.array([10, 15, 20, 25, 30])
result = np.where(arr_wh > 20)  # Returns indices where condition is True
print(result)
# Output: (array([3, 4]),) → Indices where values are greater than 20

filtered_arr = arr_wh[result]  # Apply condition
print(filtered_arr)
# Output: [25 30]

arr_where = np.array([10, 15, 20, 25, 30])
new_arr = np.where(arr_where > 20, 99, arr_where)  # Replace values > 20 with 99
print(new_arr)
# Output: [10 15 20 99 99]

arr = np.array([1, 5, 7, 9, 2, 6])
modified_arr = np.where(arr > 5, arr * 2, arr)
print(modified_arr)
# Output:
# [ 1  5 14 18  2 12]

arr2D = np.array([[5, 15, 20], [8, 10, 25]])
indices = np.where(arr2D > 10)
print(indices)
# (array([0, 0, 1]), array([1, 2, 2])) -> (row indices, col indices)
print(arr2D[indices])
# Output:
# [15 20 25]

arr2D = np.array([[5, 15, 20], [8, 10, 25]])
arr2D = np.where(arr2D > 10, -1, arr2D)
print(arr2D)
# Output:
# [[ 5 -1 -1]
#  [ 8 10 -1]]

arr = np.array([1, 2, 3, 4, 5, 6])
even_indices = np.where(arr % 2 == 0)
print(even_indices)
print(arr[even_indices])
# Output:
# (array([1, 3, 5]),)
# [2 4 6]

arr = np.array([1, 5, 10, 15, 20, 25])
result = np.where((arr > 5) & (arr < 20))
print(arr[result])
# Output:
# [10 15]

arr = np.array([1, 5, 10, 15, 20, 25])
labels = np.where(arr < 5, "low",
         np.where(arr <= 15, "medium", "high"))
print(labels)
# Output:
# ['low' 'medium' 'medium' 'medium' 'high' 'high']

# **********************************************************************************************************************

# Looping Through an Array
arr_f = np.array([1, 2, 3, 4])
for num in arr_f:
    print(num)
# Output:
# 1
# 2
# 3
# 4

arr2D_f = np.array([[1, 2, 3], [4, 5, 6]])
for row in arr2D_f:
    print(row)
# Output:
# [1 2 3]
# [4 5 6]

# Looping Over Each Element (Flattened)
arr2D_for = np.array([[1, 2, 3], [4, 5, 6]])

for num in np.nditer(arr2D_for):
    print(num)
# Output:
# 1
# 2
# 3
# 4
# 5
# 6

# **********************************************************************************************************************

# Crating a data frame from arrays
employee_ID = np.array([101, 102, 103, 104, 105])
name = np.array(['Alice', 'Bob', 'Charlie', 'David', 'Eva'], dtype=object)
age = np.array([28, 34, 29, 45, 38])

df = pd.DataFrame({'Employee_ID': employee_ID, 'Name': name, 'Age': age})


# Creating a DataFrame using a list of columns
cols = ['Employee_ID', 'Name', 'Age']
data = np.column_stack((employee_ID, name, age))  # Stack arrays column-wise

df_stacked = pd.DataFrame(data, columns=cols)

# Output:
#   Employee_ID     Name Age
# 0         101    Alice  28
# 1         102      Bob  34
# 2         103  Charlie  29
# 3         104    David  45
# 4         105      Eva  38

# **********************************************************************************************************************

# Creating an array from a series
df_company = pd.DataFrame({
    'Employee_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva']})

arr_id = np.array(df_company['Employee_ID'])
arr_name = np.array(df_company['Name'], dtype='object')

print(arr_id)
print(arr_id.shape)
# [101 102 103 104 105]
# (5,)

print(arr_name)
print(arr_name.shape)
# ['Alice' 'Bob' 'Charlie' 'David' 'Eva']
# (5,)

# **********************************************************************************************************************
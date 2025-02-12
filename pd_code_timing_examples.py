import time

# Function to generate a list of squares
def generate_squares(n):
    return [i ** 2 for i in range(n)]

# Function to find the sum of a list
def sum_list(lst):
    return sum(lst)

# Function to combine both tasks: generate squares and sum them
def compute_sum_of_squares(n):
    squares = generate_squares(n)
    total = sum_list(squares)
    return total

# Timing the entire process
n = 100000  # Input size
start_time = time.time()

# Execute the function
result = compute_sum_of_squares(n)

# End the timer
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print(f"Result: {result}")
print(f"Total execution time: {elapsed_time:.6f} seconds")


# Timing individual components
# 1. Timing generate_squares
start_time = time.time()
squares = generate_squares(n)
end_time = time.time()
print(f"Time to generate squares: {end_time - start_time:.6f} seconds")

# 2. Timing sum_list
start_time = time.time()
total = sum_list(squares)
end_time = time.time()
print(f"Time to sum squares: {end_time - start_time:.6f} seconds")
print()
# Result: 333328333350000
# Total execution time: 0.032192 seconds
# Time to generate squares: 0.028032 seconds
# Time to sum squares: 0.002998 seconds
# **********************************************************************************************************************

# Define the range for the loop
n = 100000

# Start the timer
start_time = time.time()

# Run the loop
total = 0
for i in range(1, n + 1):
    total += i  # Simple summation

# End the timer
end_time = time.time()

# Calculate and display elapsed time
elapsed_time = end_time - start_time
print(f"Execution time for summing numbers up to {n}: {elapsed_time:.6f} seconds")
# Execution time for summing numbers up to 100000: 0.010994 seconds
# **********************************************************************************************************************

import timeit

# Function to generate a list of squares
def generate_squares(n):
    return [i ** 2 for i in range(n)]

# Function to find the sum of a list
def sum_list(lst):
    return sum(lst)

# Function to combine both tasks: generate squares and sum them
def compute_sum_of_squares(n):
    squares = generate_squares(n)
    total = sum_list(squares)
    return total

# globals=globals(): Ensures that the timeit.timeit() function has access to the variables (n, squares)
# and functions (compute_sum_of_squares, etc.) in your script.
# number=1: Specifies that each function is executed only once for the timing.
# Modular Timing: The total time for compute_sum_of_squares is measured, as well as the individual times for generate_squares and sum_list.

# Input size
n = 100000

# Timing the entire process
total_time = timeit.timeit("compute_sum_of_squares(n)", globals=globals(), number=1)
print(f"Total execution time (compute_sum_of_squares): {total_time:.6f} seconds")

# Timing individual components
# 1. Timing generate_squares
generate_squares_time = timeit.timeit("generate_squares(n)", globals=globals(), number=1)
print(f"Time to generate squares: {generate_squares_time:.6f} seconds")

# 2. Timing sum_list
# First, we need to generate the squares before timing sum_list
squares = generate_squares(n)  # Prepare input
sum_list_time = timeit.timeit("sum_list(squares)", globals=globals(), number=1)
print(f"Time to sum squares: {sum_list_time:.6f} seconds")
# Total execution time (compute_sum_of_squares): 0.031618 seconds
# Time to generate squares: 0.030657 seconds
# Time to sum squares: 0.002717 seconds
# **********************************************************************************************************************

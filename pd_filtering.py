import pandas as pd

pd.options.display.width = 0

# Use loc with logical operators when you need to create more complex conditions
# that involve combinations of equality checks or custom logic,
# especially when the conditions are not limited to a set of possible values.

# Use isin() when you need to check if a SINGLE column's values match one or more possible values.
# It's the preferred option for clarity and conciseness.

data = {'id': [101, 102, 103, 104, 105, 106, 107],
        'rate': [21, 21, 19, 25, 34, 20, 23],
        'type': ['W2', 'W2', 'W2', 'W2', 1099, 1099, 'NA'],
        'status': ['active', 'active', 'hold', 'active', 'active', 'hold', 'inactive'],
        'age': [21, 19, 33, 36, 34, 20, 45],
        'degree': [False, False, True, False, True, True, True]}
df = pd.DataFrame(data)

# Filtering Data Using loc
# df.loc[rows, cols] can except column names or index

# Filter Rows Based on a Single Condition: status == active
df_single = df.loc[df['status'] == 'active']

# Output:
#     id  rate  type  status  age  degree
# 0  101    21    W2  active   21   False
# 1  102    21    W2  active   19   False
# 3  104    25    W2  active   36   False
# 4  105    34  1099  active   34    True

# Filter Rows Based on Multiple Conditions
filtered_status_rate = (df['status'] == 'active') & (df['rate'] > 24)
df_mult = df.loc[filtered_status_rate]

# Output:
#     id  rate  type  status  age  degree
# 3  104    25    W2  active   36   False
# 4  105    34  1099  active   34    True

# Select Specific Rows and Columns
cols = ['id', 'status', 'degree', 'age']
rows = (df['degree'] == False) & (df['age'] <= 21)
df_rows_cols = df.loc[rows, cols]

# Output:
#     id  status  degree  age
# 0  101  active   False   21
# 1  102  active   False   19

# Update Values Using. 10% rate increase for employees with degree
# Ensure 'rate' column is float before the operation
df['rate'] = df['rate'].astype(float)
# The *= operator does not return a new DataFrame or Series; instead, it modifies the DataFrame directly: use copy().
df.loc[df['degree'] == True, 'rate'] *= 1.1
# Create a new DataFrame after the update
df_update = df.copy()

# Output:
#     id  rate  type    status  age  degree
# 0  101  21.0    W2    active   21   False
# 1  102  21.0    W2    active   19   False
# 2  103  20.9    W2      hold   33    True
# 3  104  25.0    W2    active   36   False
# 4  105  37.4  1099    active   34    True
# 5  106  22.0  1099      hold   20    True
# 6  107  25.3    NA  inactive   45    True

# Filter Rows Using Index and Column Names
# it requires column labels (column names) for column selection.
df = df.loc[0:4, ['id', 'status', 'degree', 'age']]

# Output:
#     id  status  degree  age
# 0  101  active   False   21
# 1  102  active   False   19
# 2  103    hold    True   33
# 3  104  active   False   36
# 4  105  active    True   34
# **********************************************************************************************************************

# Filter rows where 'status' is either 'active' or 'inactive' by using isin()
df_status_isin = df[df['status'].isin(['active', 'inactive'])]
# SAME RESULT WITH LOC
# Using loc to filter rows where 'status' is 'active' or 'inactive'
df_status_loc = df.loc[(df['status'] == 'active') | (df['status'] == 'inactive')]

print(df_status_isin)
# Output:
#     id  rate  type    status  age  degree
# 0  101    21    W2    active   21   False
# 1  102    21    W2    active   19   False
# 3  104    25    W2    active   36   False
# 4  105    34  1099    active   34    True
# 6  107    23    NA  inactive   45    True

# Filter rows where 'status' is either 'active' or 'inactive' and 'age' is 21 or older
df_isin = df[(df['status'].isin(['active', 'inactive'])) & (df['age'] >= 21)]
# SAME RESULT WITH LOC
# Using loc to filter rows where 'status' is 'active' or 'inactive' and 'age' is 21 or older
df_loc = df.loc[(df['status'] == 'active') | (df['status'] == 'inactive') & (df['age'] >= 21)]

# Output:
#     id  rate  type    status  age  degree
# 0  101    21    W2    active   21   False
# 3  104    25    W2    active   36   False
# 4  105    34  1099    active   34    True
# 6  107    23    NA  inactive   45    True
# **********************************************************************************************************************

# Vectorized Solution for Single Condition
# Vectorized operation to assign 500 to NEW COLUMN 'bonus' where 'type' is 'W2'
df.loc[df['type'] == 'W2', 'bonus'] = 500


# Vectorized Solution for Multiple Conditions
df.loc[(df['degree'] == True) & (df['type'] == 'W2'), 'race'] = 'approved'
# **********************************************************************************************************************



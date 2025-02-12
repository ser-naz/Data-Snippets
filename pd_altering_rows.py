import pandas as pd

# Sample DataFrame for row alterations practice
df_company = pd.DataFrame({
    'Employee_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [28, 34, 29, 45, 38],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'IT'],
    'Salary': [50000, 60000, 55000, 70000, 65000],
    'Is_Manager': [False, True, False, True, False]})

# Display the DataFrame
print(df_company)
#    Employee_ID     Name  Age Department  Salary  Is_Manager
# 0          101    Alice   28         HR   50000       False
# 1          102      Bob   34         IT   60000        True
# 2          103  Charlie   29    Finance   55000       False
# 3          104    David   45  Marketing   70000        True
# 4          105      Eva   38         IT   65000       False
# **********************************************************************************************************************

# Updating One Value in a Row using .loc[]
df_company.loc[1, 'Salary'] = 62000  # Update Salary for Bob (index 1)
print('\n',df_company)
#     Employee_ID     Name  Age Department  Salary  Is_Manager
# 0          101    Alice   28         HR   50000       False
# 1          102      Bob   34         IT   62000 *      True
# 2          103  Charlie   29    Finance   55000       False
# 3          104    David   45  Marketing   70000        True
# 4          105      Eva   38         IT   65000       False

# Updating One Value in a Row .at[]
df_company.at[1, 'Age'] = 36  # Change Bob's age to 36
print('\n',df_company)
#     Employee_ID     Name  Age Department  Salary  Is_Manager
# 0          101    Alice   28         HR   50000       False
# 1          102      Bob   36 *       IT   62000        True
# 2          103  Charlie   29    Finance   55000       False
# 3          104    David   45  Marketing   70000        True
# 4          105      Eva   38         IT   65000       False

# Updating Two Values in a Row
df_company.loc[1, ['Age', 'Salary']] = [34, 60000]  # Update Age and Department for Bob (index 1)
print('\n',df_company)
#     Employee_ID     Name  Age Department  Salary  Is_Manager
# 0          101    Alice   28         HR   50000       False
# 1          102      Bob   34 *       IT   60000 *      True
# 2          103  Charlie   29    Finance   55000       False
# 3          104    David   45  Marketing   70000        True
# 4          105      Eva   38         IT   65000       False

# Update the entire row for Charlie (index 2)
df_company.loc[1] = [102, 'Bobby', 35, 'Operation', 61575, False]  # Update all columns for Charlie
print('\n',df_company)
#     Employee_ID     Name  Age Department  Salary  Is_Manager
# 0          101    Alice   28         HR   50000       False
# 1          102    Bobby * 35 * Operation  61575 *     False *
# 2          103  Charlie   29    Finance   55000       False
# 3          104    David   45  Marketing   70000        True
# 4          105      Eva   38         IT   65000       False


# update all value in one COLUMN
df_company_col = df_company.copy()
df_company_col['Is_Manager'] = df_company_col['Is_Manager'].astype(str)
df_company_col.loc[:, 'Is_Manager'] = ['No', 'Assistant Manager', 'Not Manager', 'Yes', 'False']
print('\n',df_company_col)
#     Employee_ID     Name  Age Department  Salary         Is_Manager
# 0          101    Alice   28         HR   50000                 No
# 1          102    Bobby   35  Operation   61575  Assistant Manager
# 2          103  Charlie   29    Finance   55000        Not Manager
# 3          104    David   45  Marketing   70000                Yes
# 4          105      Eva   38         IT   65000              False
# **********************************************************************************************************************

# vectorized operation
# Update the Department for Employee_ID 101 (Alice) from 'HR' to 'Payroll'
df_company.loc[df_company['Employee_ID'] == 101, 'Department'] = 'Payroll'
print('\n',df_company)
#     Employee_ID     Name  Age Department  Salary  Is_Manager
# 0          101    Alice   28    Payroll * 50000       False
# 1          102    Bobby   35  Operation   61575       False
# 2          103  Charlie   29    Finance   55000       False
# 3          104    David   45  Marketing   70000        True
# 4          105      Eva   38         IT   65000       False

# Update both Department and Salary for Employee_ID 101 (Alice)
df_company.loc[df_company['Employee_ID'] == 104, ['Department', 'Salary']] = ['Sales', 72500]
print('\n',df_company)
#     Employee_ID     Name  Age Department  Salary  Is_Manager
# 0          101    Alice   28    Payroll   50000       False
# 1          102    Bobby   35  Operation   61575       False
# 2          103  Charlie   29    Finance   55000       False
# 3          104    David   45      Sales   72500        True
# 4          105      Eva   38         IT   65000       False
# **********************************************************************************************************************

# Updating Values Using Row and Column Indexes
df_company.iloc[1, 1] = 'Bob'
print('\n',df_company)
#     Employee_ID     Name  Age Department  Salary  Is_Manager
# 0          101    Alice   28    Payroll   50000       False
# 1          102      Bob * 35  Operation   61575       False
# 2          103  Charlie   29    Finance   55000       False
# 3          104    David   45      Sales   72500        True
# 4          105      Eva   38         IT   65000       False
# **********************************************************************************************************************

# ADDING NEW VALUES
# Adding a New Row using loc[]
df_company.loc[5] = [106, 'Frank', 41, 'HR', 62000, False]  # Add a new row at index 5 for Frank

# Dynamically add a new row at the next available index
df_company.loc[len(df_company)] = [107, 'John', 45, 'Intake', 31000, False]
print('\n',df_company)

#     Employee_ID     Name  Age Department  Salary  Is_Manager
# 0          101    Alice   28    Payroll   50000       False
# 1          102      Bob   35  Operation   61575       False
# 2          103  Charlie   29    Finance   55000       False
# 3          104    David   45      Sales   72500        True
# 4          105      Eva   38         IT   65000       False
# 5          106    Frank   41         HR   62000       False
# 6          107     John   45     Intake   31000       False


# Can't insert a row in-place with a simple method in pandas
# New row to insert at index 0
# New data frame has to created and concat with the original data frame
df_new_row = pd.DataFrame([[100, 'Mary', 61, 'HR', 95000, True]], columns=df_company.columns)

# Concatenate the first part (up to index 0), df_new_row, and the rest
df_company = pd.concat([df_company.iloc[:0], df_new_row, df_company.iloc[0:]], ignore_index=True)

print('\n',df_company)
#     Employee_ID     Name  Age Department  Salary  Is_Manager
# 0          100     Mary   61         HR   95000        True
# 1          101    Alice   28    Payroll   50000       False
# 2          102      Bob   35  Operation   61575       False
# 3          103  Charlie   29    Finance   55000       False
# 4          104    David   45      Sales   72500        True
# 5          105      Eva   38         IT   65000       False
# 6          106    Frank   41         HR   62000       False
# 7          107     John   45     Intake   31000       False
# **********************************************************************************************************************

# totals on the bottom of the data set



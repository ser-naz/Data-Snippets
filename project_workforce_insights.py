import pandas as pd
pd.options.display.width = 0

# **********************************************************************************************************************
# Employee Performance & Compensation Analysis PROJECT
# groupby emphasis
# **********************************************************************************************************************

# Creating the DataFrame
data = {
    "Employee": ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Alice", "Bob", "Charlie"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "IT", "HR", "IT"],
    "Hire Date": ["2018-05-21", "2020-08-15", "2016-03-10", "2019-07-01", "2021-09-05", "2017-11-20", "2022-02-17",
                  "2018-05-21", "2020-08-15", "2016-03-10"],
    "Salary": [75000, 55000, 80000, 72000, 60000, 90000, 68000, 75000, 55000, 80000],
    "Bonus (%)": [10, 5, 12, 8, 4, 15, 6, 10, 5, 12],
    "Performance Score": [4.5, 3.8, 4.9, 4.2, 3.5, 4.7, 3.9, 4.5, 3.8, 4.9],
    "Date": ["2024-01-03", "2024-01-03", "2024-01-03", "2024-01-03", "2024-01-04", "2024-01-04", "2024-01-04",
             "2024-01-05", "2024-01-05", "2024-01-05"],
    "Hours Worked": [8, 7, 9, 6, 5, 8, 7, 9, 8, 7],
    "Hourly Rate": [50, 30, 55, 40, 32, 60, 38, 50, 30, 55]}

df = pd.DataFrame(data)

# Convert columns to appropriate types
df['Hire Date'] = pd.to_datetime(df['Hire Date'])
df['Date'] = pd.to_datetime(df['Date'])

# Calculate additional fields
# Calculate "Years Worked"
today = pd.Timestamp.today()
df['Years Worked'] = ((today - df['Hire Date']) / pd.Timedelta(days=365)).round(1)
# Calculate "Years Worked"
df["Total Compensation"] = df['Salary'] * (1 + df['Bonus (%)'] / 100)
# Calculate Earnings
df['Earnings'] = df['Hours Worked'] * df['Hourly Rate']

#   Employee Department  Hire Date  Salary  Bonus (%)  Performance Score       Date  Hours Worked  Hourly Rate  Years Worked  Total Compensation  Earnings
# 0    Alice         IT 2018-05-21   75000         10                4.5 2024-01-03             8           50           6.7             82500.0       400
# 1      Bob         HR 2020-08-15   55000          5                3.8 2024-01-03             7           30           4.5             57750.0       210
# 2  Charlie         IT 2016-03-10   80000         12                4.9 2024-01-03             9           55           8.9             89600.0       495
# 3    David    Finance 2019-07-01   72000          8                4.2 2024-01-03             6           40           5.6             77760.0       240
# 4     Emma         HR 2021-09-05   60000          4                3.5 2024-01-04             5           32           3.4             62400.0       160
# 5    Frank         IT 2017-11-20   90000         15                4.7 2024-01-04             8           60           7.2            103500.0       480
# 6    Grace    Finance 2022-02-17   68000          6                3.9 2024-01-04             7           38           3.0             72080.0       266
# 7    Alice         IT 2018-05-21   75000         10                4.5 2024-01-05             9           50           6.7             82500.0       450
# 8      Bob         HR 2020-08-15   55000          5                3.8 2024-01-05             8           30           4.5             57750.0       240
# 9  Charlie         IT 2016-03-10   80000         12                4.9 2024-01-05             7           55           8.9             89600.0       385


# Group by Department and apply multiple aggregation functions to the Salary column
aggregated_data = df.groupby("Department")["Salary"].agg(["mean", "sum", "count"]).reset_index()

print(aggregated_data, '\n')
#   Department          mean     sum  count
# 0    Finance  70000.000000  140000      2
# 1         HR  56666.666667  170000      3
# 2         IT  80000.000000  400000      5

# Find the department with the highest average performance score.
top_department = df.groupby("Department")["Performance Score"].mean().idxmax()
highest_score = df.groupby("Department")["Performance Score"].mean().max()

print(f"\n{top_department} department has the highest average performance score - {highest_score:.2f}.")
# IT department has the highest average performance score - 4.70.

# Identify the top 3 employees with the highest total compensation.
# Find top 3 employees with the highest total compensation
top_3_employees = df.nlargest(3, "Total Compensation")["Employee"].tolist()
print(f"\nTop 3 employees with the highest total compensation: {', '.join(top_3_employees)}.")
# Top 3 employees with the highest total compensation: Frank, Charlie, Charlie.

# Determine the employee with the highest total earnings across all records.
top_paid_emp = df.groupby("Employee")["Earnings"].sum().idxmax()
top_amount = df.groupby("Employee")["Earnings"].sum().max()

print(f'\n{top_paid_emp} is the employee with the highest total earnings, making {top_amount:.2f}.')
# Charlie is the employee with the highest total earnings, making 880.00.

# Find the department with the highest total hours worked.
top_hours_dep = df.groupby("Department")["Hours Worked"].sum().idxmax()
print(f'\n{top_hours_dep} department has the highest total hours worked.')
# IT department has the highest total hours worked.

# Find the employee who worked the most hours in a single day.
# Group by "Date" and find the employee with the max hours for each day
top_hours_per_day = df.loc[df.groupby("Date")["Hours Worked"].idxmax(), ["Date", "Employee", "Hours Worked"]]
print('\n', top_hours_per_day)
#          Date Employee  Hours Worked
# 2 2024-01-03  Charlie             9
# 5 2024-01-04    Frank             8
# 7 2024-01-05    Alice             9

# Determine average Earnings per department
earnings_per_dep = df.groupby('Department')['Earnings'].mean().reset_index()
print('\n', earnings_per_dep)
#    Department    Earnings
# 0    Finance  253.000000
# 1         HR  203.333333
# 2         IT  442.000000


# Analyze whether there's a correlation between performance score and earnings.

# If the correlation is close to 1, there's a strong positive relationship.
# If it's close to 0, there's no real correlation.
# If it's close to -1, it’s a negative correlation (unlikely in this case).

# Determine average performance score per department
performance_per_dep = df.groupby('Department')['Performance Score'].mean().reset_index()
print('\n', performance_per_dep)
#    Department  Performance Score
# 0    Finance               4.05
# 1         HR               3.70
# 2         IT               4.70

# correlation between earnings and performance score
correlation = earnings_per_dep['Earnings'].corr(performance_per_dep['Performance Score'])
print(f"\nCorrelation between earnings and performance score: {correlation:.2f}")
# Correlation between earnings and performance score: 0.99

# Calculate the Percentage of Total Hours Worked by Each Department
# shows what percentage of the total hours worked belongs to each employee.
df['Total Hours Share (%)'] = df.groupby("Department")["Hours Worked"].transform(lambda x: (x / x.sum()) * 100)
print("\nDepartment-wise share of total hours worked:\n", df[['Employee', 'Department', 'Hours Worked', 'Total Hours Share (%)']])
# Department-wise share of total hours worked:
#    Employee Department  Hours Worked  Total Hours Share (%)
# 0    Alice         IT             8              19.512195
# 1      Bob         HR             7              35.000000
# 2  Charlie         IT             9              21.951220
# 3    David    Finance             6              46.153846
# 4     Emma         HR             5              25.000000
# 5    Frank         IT             8              19.512195
# 6    Grace    Finance             7              53.846154
# 7    Alice         IT             9              21.951220
# 8      Bob         HR             8              40.000000
# 9  Charlie         IT             7              17.073171

# Find the Most Overworked Employee (Max Hours Worked in Total)
most_overworked_emp = df.groupby("Employee")["Hours Worked"].sum().idxmax()
most_hours = df.groupby("Employee")["Hours Worked"].sum().max()

print(f"\n{most_overworked_emp} is the most overworked employee with {most_hours} hours worked.")
# Alice is the most overworked employee with 17 hours worked.

# Rank Employees Based on Their Performance Within Each Department
# assigns a rank to employees within their department based on performance.
df["Performance Rank"] = df.groupby("Department")["Performance Score"].rank(ascending=False, method="dense")
print("\nEmployee rankings within each department based on performance:\n", df[['Employee', 'Department', 'Performance Score', 'Performance Rank']])
# Employee rankings within each department based on performance:
#    Employee Department  Performance Score  Performance Rank
# 0    Alice         IT                4.5               3.0
# 1      Bob         HR                3.8               1.0
# 2  Charlie         IT                4.9               1.0
# 3    David    Finance                4.2               1.0
# 4     Emma         HR                3.5               2.0
# 5    Frank         IT                4.7               2.0
# 6    Grace    Finance                3.9               2.0
# 7    Alice         IT                4.5               3.0
# 8      Bob         HR                3.8               1.0
# 9  Charlie         IT                4.9               1.0

# Rank Employees Based on Their Performance Within Each Department
# Identifies employees who frequently work overtime
df["Overtime Hours"] = df["Hours Worked"].apply(lambda x: x - 7 if x > 7 else 0)
print('\n', df[["Employee", "Overtime Hours"]])
#    Employee  Overtime Hours
# 0    Alice               1
# 1      Bob               0
# 2  Charlie               2
# 3    David               0
# 4     Emma               0
# 5    Frank               1
# 6    Grace               0
# 7    Alice               2
# 8      Bob               1
# 9  Charlie               0

overtime_per_employee = df.groupby("Employee")["Overtime Hours"].sum().reset_index()

print("\nTotal overtime hours worked per employee:\n", overtime_per_employee)
# Total overtime hours worked per employee:
#    Employee  Overtime Hours
# 0    Alice               3
# 1      Bob               1
# 2  Charlie               2
# 3    David               0
# 4     Emma               0
# 5    Frank               1
# 6    Grace               0


# Group by both Department and Employee and calculate the total Hours Worked for each combination
total_hours_multi_group = df.groupby(["Department", "Employee"])["Hours Worked"].sum()

# Display the result
print('\n', total_hours_multi_group)
#  Department  Employee
# Finance     David        6
#             Grace        7
# HR          Bob         15
#             Emma         5
# IT          Alice       17
#             Charlie     16
#             Frank        8
# Name: Hours Worked, dtype: int64

# Retrieve total hours worked by employees in the IT department
it_data = total_hours_multi_group.loc["IT"].reset_index()

# Display the result
print('\n', it_data)
#    Employee  Hours Worked
# 0    Alice            17
# 1  Charlie            16
# 2    Frank             8

import pandas as pd

"""
This project focuses on reshaping a dataset from a long format to a wide format. 
The goal is to reorganize the data to make it easier to analyze, 
with the final output presented in a more structured and summarized format, 
allowing for better comparison and reporting across different groups or periods.
"""

pd.set_option('future.no_silent_downcasting', True)
pd.options.display.width = 0

report = {
    'Code Type': ['3 -T', '1 - E', '3 -T', '3 -T', '3 -T', '3 -T', '3 -T', '1 - E', '3 -T', '3 -T', '1 - E', '3 -T',
                  '3 -T', '3 -T', '3 -T', '3 -T', '3 -T', '2-D', '2-D'],
    'Code': ['FWT', 'HOURLY', 'MEDI', 'NYLOC', 'NYPFL', 'NYSDI', 'NYSIT', 'OT', 'SSEC', 'FWT', 'HOURLY', 'MEDI',
             'NYLOC', 'NYPFL', 'NYSDI', 'NYSIT', 'SSEC', 'HEALTH', '401K'],
    'Check Number': [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9998, 9998, 9998, 9998, 9998, 9998, 9998,
                     9998, 9998, 9998],
    'Full Name': ['empl_one', 'empl_one', 'empl_one', 'empl_one', 'empl_one', 'empl_one', 'empl_one', 'empl_one',
                  'empl_one', 'empl_two', 'empl_two', 'empl_two', 'empl_two', 'empl_two', 'empl_two', 'empl_two',
                  'empl_two', 'empl_two', 'empl_two'],
    'Employee Number': [101, 101, 101, 101, 101, 101, 101, 101, 101, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102],
    'Department': ['HR', 'HR', 'HR', 'HR', 'HR', 'HR', 'HR', 'HR', 'HR', 'Sales', 'Sales', 'Sales', 'Sales', 'Sales',
                   'Sales', 'Sales', 'Sales', 'Sales', 'Sales'],
    'Check Date': [pd.Timestamp('2025-02-07 00:00:00'), pd.Timestamp('2025-02-07 00:00:00'),
                   pd.Timestamp('2025-02-07 00:00:00'),
                   pd.Timestamp('2025-02-07 00:00:00'), pd.Timestamp('2025-02-07 00:00:00'),
                   pd.Timestamp('2025-02-07 00:00:00'),
                   pd.Timestamp('2025-02-07 00:00:00'), pd.Timestamp('2025-02-07 00:00:00'),
                   pd.Timestamp('2025-02-07 00:00:00'),
                   pd.Timestamp('2025-02-07 00:00:00'), pd.Timestamp('2025-02-07 00:00:00'),
                   pd.Timestamp('2025-02-07 00:00:00'),
                   pd.Timestamp('2025-02-07 00:00:00'), pd.Timestamp('2025-02-07 00:00:00'),
                   pd.Timestamp('2025-02-07 00:00:00'),
                   pd.Timestamp('2025-02-07 00:00:00'), pd.Timestamp('2025-02-07 00:00:00'),
                   pd.Timestamp('2025-02-07 00:00:00'),
                   pd.Timestamp('2025-02-07 00:00:00')],
    'Period End': [pd.Timestamp('2025-01-31 00:00:00'), pd.Timestamp('2025-01-31 00:00:00'),
                   pd.Timestamp('2025-01-31 00:00:00'),
                   pd.Timestamp('2025-01-31 00:00:00'), pd.Timestamp('2025-01-31 00:00:00'),
                   pd.Timestamp('2025-01-31 00:00:00'),
                   pd.Timestamp('2025-01-31 00:00:00'), pd.Timestamp('2025-01-31 00:00:00'),
                   pd.Timestamp('2025-01-31 00:00:00'),
                   pd.Timestamp('2025-01-31 00:00:00'), pd.Timestamp('2025-01-31 00:00:00'),
                   pd.Timestamp('2025-01-31 00:00:00'),
                   pd.Timestamp('2025-01-31 00:00:00'), pd.Timestamp('2025-01-31 00:00:00'),
                   pd.Timestamp('2025-01-31 00:00:00'),
                   pd.Timestamp('2025-01-31 00:00:00'), pd.Timestamp('2025-01-31 00:00:00'),
                   pd.Timestamp('2025-01-31 00:00:00'),
                   pd.Timestamp('2025-01-31 00:00:00')],
    'Total Net Pay': [1420.36, 1420.36, 1420.36, 1420.36, 1420.36, 1420.36, 1420.36, 1420.36, 1420.36, 1741.14, 1741.14,
                      1741.14, 1741.14, 1741.14, 1741.14, 1741.14, 1741.14, 1741.14, 1741.14],
    'Amount': [72.0, 1528.0, 25.48, 51.96, 6.82, 1.2, 70.43, 229.2, 108.95, 110.3, 2019.32, 31.84, 6.59, 8.95, 1.2,
               110.3, 136.16, 150.0, 55.0],
    'Hours': [0, 80, 0, 0, 0, 0, 0, 8, 0, 0, 80, 0, 0, 0, 0, 0, 0, 0, 0],
    'Earnings': [0.0, 1528.0, 0.0, 0.0, 0.0, 0.0, 0.0, 229.2, 0.0, 0.0, 2019.32, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                 0.0]}

df_report = pd.DataFrame(report)

#    Code Type    Code  Check Number Full Name  Employee Number Department Check Date Period End  Total Net Pay   Amount  Hours  Earnings
# 0       3 -T     FWT          9999  empl_one              101         HR 2025-02-07 2025-01-31        1420.36    72.00      0      0.00
# 1      1 - E  HOURLY          9999  empl_one              101         HR 2025-02-07 2025-01-31        1420.36  1528.00     80   1528.00
# 2       3 -T    MEDI          9999  empl_one              101         HR 2025-02-07 2025-01-31        1420.36    25.48      0      0.00
# 3       3 -T   NYLOC          9999  empl_one              101         HR 2025-02-07 2025-01-31        1420.36    51.96      0      0.00
# 4       3 -T   NYPFL          9999  empl_one              101         HR 2025-02-07 2025-01-31        1420.36     6.82      0      0.00
# 5       3 -T   NYSDI          9999  empl_one              101         HR 2025-02-07 2025-01-31        1420.36     1.20      0      0.00
# 6       3 -T   NYSIT          9999  empl_one              101         HR 2025-02-07 2025-01-31        1420.36    70.43      0      0.00
# 7      1 - E      OT          9999  empl_one              101         HR 2025-02-07 2025-01-31        1420.36   229.20      8    229.20
# 8       3 -T    SSEC          9999  empl_one              101         HR 2025-02-07 2025-01-31        1420.36   108.95      0      0.00
# 9       3 -T     FWT          9998  empl_two              102      Sales 2025-02-07 2025-01-31        1741.14   110.30      0      0.00
# 10     1 - E  HOURLY          9998  empl_two              102      Sales 2025-02-07 2025-01-31        1741.14  2019.32     80   2019.32
# 11      3 -T    MEDI          9998  empl_two              102      Sales 2025-02-07 2025-01-31        1741.14    31.84      0      0.00
# 12      3 -T   NYLOC          9998  empl_two              102      Sales 2025-02-07 2025-01-31        1741.14     6.59      0      0.00
# 13      3 -T   NYPFL          9998  empl_two              102      Sales 2025-02-07 2025-01-31        1741.14     8.95      0      0.00
# 14      3 -T   NYSDI          9998  empl_two              102      Sales 2025-02-07 2025-01-31        1741.14     1.20      0      0.00
# 15      3 -T   NYSIT          9998  empl_two              102      Sales 2025-02-07 2025-01-31        1741.14   110.30      0      0.00
# 16      3 -T    SSEC          9998  empl_two              102      Sales 2025-02-07 2025-01-31        1741.14   136.16      0      0.00
# 17       2-D  HEALTH          9998  empl_two              102      Sales 2025-02-07 2025-01-31        1741.14   150.00      0      0.00
# 18       2-D    401K          9998  empl_two              102      Sales 2025-02-07 2025-01-31        1741.14    55.00      0      0.00


# A new column Code is created by combining the last character of the Code Type column with the Code column
# will be used for sorting later
df_report['Code'] = df_report['Code Type'].str[-1] + '-' + df_report['Code']

# The original Code Type column is removed from the dataframe after creating the new Code column
df_report = df_report.drop(columns='Code Type')

# Calculate the Start Date as 20 days before the Check Date
df_report['Start Date'] = df_report['Check Date'] - pd.Timedelta(days=20)

# Create the Pay Period column by combining Start Date and Period End in the desired format
df_report['Pay Period'] = (df_report['Start Date'].dt.strftime('%m/%d/%y') + '-' +
                           df_report['Period End'].dt.strftime('%m/%d/%y'))

# Period End is removed from the dataframe after creating the Pay Period column
df_report = df_report.drop(columns='Period End')

# convert the dates in Check Date to string format
df_report['Check Date'] = df_report['Check Date'].dt.strftime('%m/%d/%y')


# Reshaping the data frame into a long format
# set index
df_report = df_report.set_index(
    ['Employee Number', 'Full Name', 'Department', 'Check Number', 'Check Date', 'Pay Period', 'Total Net Pay',
     'Code']).stack()

# filtering out rows where values are equal to zero (df_report.ne(0)), keeping only non-zero values
df_report = df_report[df_report.ne(0)].unstack(level=[-2, -1])

# The column names are renamed by mapping each multi-level column index to a string format combining both levels
df_report.columns = df_report.columns.map(lambda x: f'{x[0]} {x[1]}')

# sorting columns
df_report = df_report.reindex(sorted(df_report.columns), axis=1)

# multi - level index is reset, converting it back into regular columns
df_report.reset_index(inplace=True)

# Any remaining NaN values in the dataframe are replaced with zeros
df_report = df_report.fillna(0)

print(df_report)
#   Employee Number Full Name Department  Check Number Check Date         Pay Period  Total Net Pay D-401K Amount    D-401K Start Date D-HEALTH Amount  D-HEALTH Start Date E-HOURLY Amount E-HOURLY Earnings E-HOURLY Hours  E-HOURLY Start Date E-OT Amount E-OT Earnings E-OT Hours      E-OT Start Date T-FWT Amount     T-FWT Start Date T-MEDI Amount    T-MEDI Start Date T-NYLOC Amount   T-NYLOC Start Date T-NYPFL Amount   T-NYPFL Start Date T-NYSDI Amount   T-NYSDI Start Date T-NYSIT Amount   T-NYSIT Start Date T-SSEC Amount    T-SSEC Start Date
# 0              101  empl_one         HR          9999   02/07/25  01/18/25-01/31/25        1420.36             0                    0               0                    0          1528.0            1528.0             80  2025-01-18 00:00:00       229.2         229.2          8  2025-01-18 00:00:00         72.0  2025-01-18 00:00:00         25.48  2025-01-18 00:00:00          51.96  2025-01-18 00:00:00           6.82  2025-01-18 00:00:00            1.2  2025-01-18 00:00:00          70.43  2025-01-18 00:00:00        108.95  2025-01-18 00:00:00
# 1              102  empl_two      Sales          9998   02/07/25  01/18/25-01/31/25        1741.14          55.0  2025-01-18 00:00:00           150.0  2025-01-18 00:00:00         2019.32           2019.32             80  2025-01-18 00:00:00           0             0          0                    0        110.3  2025-01-18 00:00:00         31.84  2025-01-18 00:00:00           6.59  2025-01-18 00:00:00           8.95  2025-01-18 00:00:00            1.2  2025-01-18 00:00:00          110.3  2025-01-18 00:00:00        136.16  2025-01-18 00:00:00

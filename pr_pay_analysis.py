import pandas as pd
pd.options.display.width = 0

# **********************************************************************************************************************
# Employee Pay Analysis and Location Aggregation PROJECT
# **********************************************************************************************************************

# This project involves analyzing employee pay data, aggregating hours worked and amounts earned,
# and grouping employee locations.
# It uses pandas for data manipulation, including pivot tables, groupby operations,
# and merging datasets to provide detailed insights into employee compensation and work patterns.

data = {
    'id': [101, 101, 101, 101, 101, 101, 102, 102, 102, 102, 103, 103, 103, 103, 103, 103, 104, 104, 104, 104, 104, 105,
           105, 105, 105, 105, 105, 106],
    'name': ['emp1', 'emp1', 'emp1', 'emp1', 'emp1', 'emp1', 'emp2', 'emp2', 'emp2', 'emp2', 'emp3', 'emp3', 'emp3',
             'emp3', 'emp3', 'emp3', 'emp4', 'emp4', 'emp4', 'emp4', 'emp4', 'emp5', 'emp5', 'emp5', 'emp5', 'emp5',
             'emp5', 'emp6'],
    'pay item': ['regular', 'regular', 'regular', 'regular', 'regular', 'ot', 'regular', 'regular', 'regular',
                 'regular', 'regular', 'regular', 'regular', 'regular', 'regular', 'ot', 'regular', 'regular',
                 'regular', 'regular', 'regular', 'regular', 'regular', 'regular', 'regular', 'regular', 'ot',
                 'regular'],
    'hours': [8.0, 7.75, 8.0, 7.5, 8.0, 4.0, 8.0, 8.0, 8.5, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 3.5, 6.0, 6.0, 6.0, 5.75, 6.0,
              8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 10.0],
    'rate': [25.0, 25.0, 25.0, 25.0, 25.0, 37.5, 20.0, 20.0, 20.0, 20.0, 25.0, 25.0, 25.0, 25.0, 25.0, 37.5, 25.0, 25.0,
             25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 37.5, 30.0],
    'amount': [200.0, 193.75, 200.0, 187.5, 200.0, 150.0, 160.0, 160.0, 170.0, 160.0, 200.0, 200.0, 200.0, 200.0, 200.0,
               131.25, 150.0, 150.0, 150.0, 143.75, 150.0, 200.0, 200.0, 200.0, 200.0, 200.0, 300.0, 300.0],
    'date': ['01/01/24', '01/02/24', '01/03/24', '01/04/24', '01/05/24', '01/05/24', '01/01/24', '01/02/24', '01/03/24',
             '01/05/24', '01/01/24', '01/02/24', '01/03/24', '01/04/24', '01/05/24', '01/05/24', '01/01/24', '01/02/24',
             '01/03/24', '01/04/24', '01/05/24', '01/01/24', '01/02/24', '01/03/24', '01/04/24', '01/05/24', '01/05/24',
             '01/02/24'],
    'location': ['kings', 'kings', 'kings', 'queens', 'queens', 'queens', 'bronx', 'bronx', 'bronx', 'bronx',
                 'richmond', 'richmond', 'kings', 'bronx', 'bronx', 'bronx', 'richmond', 'richmond', 'kings', 'bronx',
                 'bronx', 'richmond', 'richmond', 'richmond', 'richmond', 'bronx', 'bronx', 'kings']}

# create a data frame
df = pd.DataFrame(data)

#      id  name pay item  hours  rate  amount      date  location
# 0   101  emp1  regular   8.00  25.0  200.00  01/01/24     kings
# 1   101  emp1  regular   7.75  25.0  193.75  01/02/24     kings
# 2   101  emp1  regular   8.00  25.0  200.00  01/03/24     kings
# 3   101  emp1  regular   7.50  25.0  187.50  01/04/24    queens
# 4   101  emp1  regular   8.00  25.0  200.00  01/05/24    queens
# 5   101  emp1       ot   4.00  37.5  150.00  01/05/24    queens
# 6   102  emp2  regular   8.00  20.0  160.00  01/01/24     bronx
# 7   102  emp2  regular   8.00  20.0  160.00  01/02/24     bronx
# 8   102  emp2  regular   8.50  20.0  170.00  01/03/24     bronx
# 9   102  emp2  regular   8.00  20.0  160.00  01/05/24     bronx
# 10  103  emp3  regular   8.00  25.0  200.00  01/01/24  richmond
# 11  103  emp3  regular   8.00  25.0  200.00  01/02/24  richmond
# 12  103  emp3  regular   8.00  25.0  200.00  01/03/24     kings
# 13  103  emp3  regular   8.00  25.0  200.00  01/04/24     bronx
# 14  103  emp3  regular   8.00  25.0  200.00  01/05/24     bronx
# 15  103  emp3       ot   3.50  37.5  131.25  01/05/24     bronx
# 16  104  emp4  regular   6.00  25.0  150.00  01/01/24  richmond
# 17  104  emp4  regular   6.00  25.0  150.00  01/02/24  richmond
# 18  104  emp4  regular   6.00  25.0  150.00  01/03/24     kings
# 19  104  emp4  regular   5.75  25.0  143.75  01/04/24     bronx
# 20  104  emp4  regular   6.00  25.0  150.00  01/05/24     bronx
# 21  105  emp5  regular   8.00  25.0  200.00  01/01/24  richmond
# 22  105  emp5  regular   8.00  25.0  200.00  01/02/24  richmond
# 23  105  emp5  regular   8.00  25.0  200.00  01/03/24  richmond
# 24  105  emp5  regular   8.00  25.0  200.00  01/04/24  richmond
# 25  105  emp5  regular   8.00  25.0  200.00  01/05/24     bronx
# 26  105  emp5       ot   8.00  37.5  300.00  01/05/24     bronx
# 27  106  emp6  regular  10.00  30.0  300.00  01/02/24     kings


# Creating a pivot table to calculate the total hours and total amount for each employee
# The table is indexed by 'id' and 'name', and sums up the 'hours' and 'amount' for each combination
df_pivot_amount = pd.pivot_table(df, index=['id', 'name'], values=['hours', 'amount'], aggfunc='sum')
df_pivot_amount.reset_index(inplace=True)
print('\n', df_pivot_amount)
#     id  name   amount  hours
# 0  101  emp1  1131.25  43.25
# 1  102  emp2   650.00  32.50
# 2  103  emp3  1131.25  43.50
# 3  104  emp4   743.75  29.75
# 4  105  emp5  1300.00  48.00
# 5  106  emp6   300.00  10.00

# Grouping and listing unique locations for each employee ID
df_location = pd.DataFrame({'id': df['id'].unique()})
df_location['location'] = [', '.join(sorted(df['location'].loc[df['id'] == x['id']].unique()))
                           for _, x in df_location.iterrows()]
print('\n', df_location)
#     id                location
# 0  101           kings, queens
# 1  102                   bronx
# 2  103  bronx, kings, richmond
# 3  104  bronx, kings, richmond
# 4  105         bronx, richmond
# 5  106                   kings

# Grouping and listing unique locations for each employee ID - same output using groupby()
df_location = df.groupby('id')['location'].unique().apply(lambda x: ', '.join(sorted(x))).reset_index()
print('\n', df_location)

# merge df_pivot_amount and df_location
df_amount_location = pd.merge(df_pivot_amount, df_location, on='id')
print('\n', df_amount_location)
#      id  name   amount  hours                location
# 0  101  emp1  1131.25  43.25           kings, queens
# 1  102  emp2   650.00  32.50                   bronx
# 2  103  emp3  1131.25  43.50  bronx, kings, richmond
# 3  104  emp4   743.75  29.75  bronx, kings, richmond
# 4  105  emp5  1300.00  48.00         bronx, richmond
# 5  106  emp6   300.00  10.00                   kings

# display hours by date
df_dates =  pd.pivot_table(df, index='id', columns='date', values='hours', aggfunc='sum')
df_dates.reset_index(inplace=True)
df_dates = df_dates.fillna(0)
print('\n',df_dates)
#  date   id  name  01/01/24  01/02/24  01/03/24  01/04/24  01/05/24
# 0     101  emp1       8.0      7.75       8.0      7.50      12.0
# 1     102  emp2       8.0      8.00       8.5      0.00       8.0
# 2     103  emp3       8.0      8.00       8.0      8.00      11.5
# 3     104  emp4       6.0      6.00       6.0      5.75       6.0
# 4     105  emp5       8.0      8.00       8.0      8.00      16.0
# 5     106  emp6       0.0     10.00       0.0      0.00       0.0

# merge df_pivot_amount, df_location, and df_dates
df_final = pd.merge(df_amount_location, df_dates, on='id')
print('\n',df_final)
#     id  name   amount  hours                location  01/01/24  01/02/24  01/03/24  01/04/24  01/05/24
# 0  101  emp1  1131.25  43.25           kings, queens       8.0      7.75       8.0      7.50      12.0
# 1  102  emp2   650.00  32.50                   bronx       8.0      8.00       8.5      0.00       8.0
# 2  103  emp3  1131.25  43.50  bronx, kings, richmond       8.0      8.00       8.0      8.00      11.5
# 3  104  emp4   743.75  29.75  bronx, kings, richmond       6.0      6.00       6.0      5.75       6.0
# 4  105  emp5  1300.00  48.00         bronx, richmond       8.0      8.00       8.0      8.00      16.0
# 5  106  emp6   300.00  10.00                   kings       0.0     10.00       0.0      0.00       0.0
# **********************************************************************************************************************

# MERGING MORE THAN 2 DATA FRAMES USING MERGE()
from functools import reduce
# List of DataFrames to merge
data_frames = [df_pivot_amount, df_location, df_dates]
# Merge all DataFrames on 'id'
df_merged = reduce(lambda left, right: pd.merge(left, right, on='id'), data_frames)
print(df_merged)
#     id  name   amount  hours                location  01/01/24  01/02/24  01/03/24  01/04/24  01/05/24
# 0  101  emp1  1131.25  43.25           kings, queens       8.0      7.75       8.0      7.50      12.0
# 1  102  emp2   650.00  32.50                   bronx       8.0      8.00       8.5      0.00       8.0
# 2  103  emp3  1131.25  43.50  bronx, kings, richmond       8.0      8.00       8.0      8.00      11.5
# 3  104  emp4   743.75  29.75  bronx, kings, richmond       6.0      6.00       6.0      5.75       6.0
# 4  105  emp5  1300.00  48.00         bronx, richmond       8.0      8.00       8.0      8.00      16.0
# 5  106  emp6   300.00  10.00                   kings       0.0     10.00       0.0      0.00       0.0
# **********************************************************************************************************************

# CONCATENATING MORE THAN TWO DATA FRAMES USING CONCAT() - same as df_merged
# Set 'id' as the INDEX for all DataFrames
df_pivot_amount.set_index('id', inplace=True)
df_location.set_index('id', inplace=True)
df_dates.set_index('id', inplace=True)

# Concatenate along columns (axis=1) based on 'id'
df_concat = pd.concat([df_pivot_amount, df_location, df_dates], axis=1)

# Reset index to make 'id' a column again
df_concat.reset_index(inplace=True)

print(df_concat)
#     id  name   amount  hours                location  01/01/24  01/02/24  01/03/24  01/04/24  01/05/24
# 0  101  emp1  1131.25  43.25           kings, queens       8.0      7.75       8.0      7.50      12.0
# 1  102  emp2   650.00  32.50                   bronx       8.0      8.00       8.5      0.00       8.0
# 2  103  emp3  1131.25  43.50  bronx, kings, richmond       8.0      8.00       8.0      8.00      11.5
# 3  104  emp4   743.75  29.75  bronx, kings, richmond       6.0      6.00       6.0      5.75       6.0
# 4  105  emp5  1300.00  48.00         bronx, richmond       8.0      8.00       8.0      8.00      16.0
# 5  106  emp6   300.00  10.00                   kings       0.0     10.00       0.0      0.00       0.0
# **********************************************************************************************************************

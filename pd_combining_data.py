import pandas as pd

# Merging two data frames by KEY - like VLOOKUP
data1 = {'id': [101, 102, 103, 104, 105],
         'rate': [21, 21, 19, 25, 34],
         'employment type': ['W2', 'W2', 'W2', 'W2', 1099],
         'status': ['active', 'active', 'active', 'active', 'active']}
df1 = pd.DataFrame(data1)

data2 = {'id': [101, 104, 105, 1010],
         'gender': ['male', 'female', 'female', 'male'],
         'status': ['active', 'inactive', 'active', 'active'],
         'title': ['cashier', 'cashier', 'director of sales', 'head cashier']}
df2 = pd.DataFrame(data2)

# df1
#     id  rate employment type  status
# 0  101    21              W2  active
# 1  102    21              W2  active
# 2  103    19              W2  active
# 3  104    25              W2  active
# 4  105    34            1099  active
# df2
#      id  gender    status              title
# 0   101    male    active            cashier
# 1   104  female  inactive            cashier
# 2   105  female    active  director of sales
# 3  1010    male    active       head cashier

# merged on two columns: id and status where same values in both data frames
# these two lines produce same output
df_comb = pd.merge(df1, df2)
df_comb_on_mult_columns = pd.merge(df1, df2, on=['id', 'status']) # how='inner' default

# Output:
#     id  rate employment type  status  gender              title
# 0  101    21              W2  active    male            cashier
# 1  105    34            1099  active  female  director of sales

# default suffixes _x and _y used if there are same columns in both data frames
df_comb_on_id = pd.merge(df1, df2, suffixes=('_l', '_r'), on='id')  # how='inner' default

# Output:
#     id  rate employment type status_l  gender  status_r              title
# 0  101    21              W2   active    male    active            cashier
# 1  104    25              W2   active  female  inactive            cashier
# 2  105    34            1099   active  female    active  director of sales

df_comb_how = pd.merge(df1, df2, suffixes=('_l', '_r'), on='id', how='outer') # how='outer'

# Output:
#      id  rate employment type status_l  gender  status_r              title
# 0   101  21.0              W2   active    male    active            cashier
# 1   102  21.0              W2   active     NaN       NaN                NaN
# 2   103  19.0              W2   active     NaN       NaN                NaN
# 3   104  25.0              W2   active  female  inactive            cashier
# 4   105  34.0            1099   active  female    active  director of sales
# 5  1010   NaN             NaN      NaN    male    active       head cashier

# joining on indices -------- like copy and paste two data sets side-by-side
df_comb_on_indices = pd.merge(df1, df2, suffixes=('_l', '_r'), left_index=True, right_index=True)

# Output:
#    id_l  rate employment type status_l  id_r  gender  status_r              title
# 0   101    21              W2   active   101    male    active            cashier
# 1   102    21              W2   active   104  female  inactive            cashier
# 2   103    19              W2   active   105  female    active  director of sales
# 3   104    25              W2   active  1010    male    active       head cashier
# **********************************************************************************************************************

# Stacking one df on top of the other df
df1 = pd.DataFrame({
    'Country': ['USA', 'France', 'Japan'],
    'Capital': ['Washington', 'Paris', 'Tokyo'],
    'Population': [331000000, 67000000, 125800000]})

df2 = pd.DataFrame({
    'Country': ['Germany', 'India', 'Italy'],
    'Capital': ['Berlin', 'New Delhi', 'Rome'],
    'Population': [83000000, 1380004385, 60260000]})

# Concatenate DataFrames vertically (stacking df on top of the other df)
df_combined = pd.concat([df1, df2], axis=0, ignore_index=True) # ignore_index=True to reset index

print("Stacked DataFrames:")
print(df_combined)

# Output:
# Stacked DataFrames:
#    Country     Capital  Population
# 0      USA  Washington   331000000
# 1   France       Paris    67000000
# 2    Japan       Tokyo   125800000
# 3  Germany      Berlin    83000000
# 4    India   New Delhi  1380004385
# 5    Italy        Rome    60260000
# **********************************************************************************************************************

import os
import glob
# Concatenating multiple excel files into one
# Folder containing Excel files
folder_path = r'C:\Users\YourName\Documents\ExcelFiles'  # Replace with folder path

# Use glob to get all Excel files in the folder
excel_files = glob.glob(os.path.join(folder_path, '*.xlsx'))

# Initialize an empty list to hold DataFrames
df_list = []

# Loop through each Excel file and read it into a DataFrame
for file in excel_files:
    df = pd.read_excel(file)  # Read the Excel file
    df_list.append(df)        # Append to the list

# Concatenate all DataFrames in the list vertically
df_combined = pd.concat(df_list, ignore_index=True)


# Another approach to contain Excel files
# Folder containing Excel files
folder_path = r'C:\Users\YourName\Documents\ExcelFiles'  # Replace with folder path

files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

df_list = []
for file in files:
    df = pd.read_excel(os.path.join(folder_path, file))
    df_list.append(df)

combined_data = pd.concat(df_list)
# **********************************************************************************************************************








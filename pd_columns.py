import pandas as pd
pd.options.display.width = 0

# Creating the DataFrame
df_country = pd.DataFrame({
    'Country': ['USA', 'France', 'Japan'],
    'Capital': ['Washington', 'Paris', 'Tokyo'],
    'Population': [331000000, 67000000, 125800000],
    'Year_Founded': [1776, 843, 660]})

# Reorder columns
df_country = df_country[['Country', 'Year_Founded', 'Population', 'Capital']]
print("\nReordered Columns:")
print(df_country)
# Reordered Columns:
#   Country  Year_Founded  Population     Capital
# 0     USA          1776   331000000  Washington
# **********************************************************************************************************************

# Drop a Column or Multiple Columns
# Fix: column name is case-sensitive, so 'Year_Founded' should be dropped instead of 'year_founded'
df_country = df_country.drop(columns=['Year_Founded'])
print("\nDropped 'Year_Founded' Column:")
print(df_country)
# Dropped 'Year_Founded' Column:
#   Country  Population     Capital
# 0     USA   331000000  Washington
# **********************************************************************************************************************

# Insert a Column at a Specific Position
df_country.insert(2, 'Official_Language', ['English', 'French', 'Japanese'])
print("\nInserted 'Official_Language' Column:")
print(df_country)
# Inserted 'Official_Language' Column:
#   Country  Population Official_Language     Capital
# 0     USA   331000000           English  Washington
# **********************************************************************************************************************

# Apply Operations Based on Column Type
# Apply a transformation only to numeric columns
for column in df_country.columns:
    if pd.api.types.is_numeric_dtype(df_country[column]):
        df_country[column] = df_country[column] / 1_000_000  # Convert to millions

print("\nUpdated DataFrame after conversion:")
print(df_country)
# Updated DataFrame after conversion:
#   Country  Population Official_Language     Capital
# 0     USA       331.0           English  Washington
# 1  France        67.0            French       Paris
# 2   Japan       125.8          Japanese       Tokyo
# **********************************************************************************************************************

# Create a Summary for Each Column
# Generate descriptive statistics for each column
for column in df_country.columns:
    if pd.api.types.is_numeric_dtype(df_country[column]):
        print(f"\nStatistics for '{column}':")
        print(f"  Mean: {df_country[column].mean()}")
        print(f"  Median: {df_country[column].median()}")
        print(f"  Sum: {df_country[column].sum()}")

# Statistics for 'Population':
#   Mean: 174.6
#   Median: 125.8
#   Sum: 523.8
# **********************************************************************************************************************

# Sum up the Population column
total_population = df_country['Population'].sum()  # can be used to find mean or median

# Print the result
print(f"\nTotal Population: {total_population}")
# Total Population: 523.8
# **********************************************************************************************************************

# Looping Through Columns
# Check for Missing Values in Each Column
for column in df_country.columns:
    missing_count = df_country[column].isnull().sum()
    print(f"Column '{column}' has {missing_count} missing values.")

# Column 'Country' has 0 missing values.
# Column 'Population' has 0 missing values.
# Column 'Official_Language' has 0 missing values.
# Column 'Capital' has 0 missing values.
# **********************************************************************************************************************

# Apply lower() for whole column
# Fix: Referencing 'df_country' instead of 'df'
for col in df_country.columns:
    try:
        df_country[col] = df_country[col].str.lower()
    except AttributeError:
        pass

print("\nDataFrame with lowercased text columns:")
print(df_country)
# DataFrame with lowercased text columns:
#   Country  Population Official_Language     Capital
# 0     usa       331.0           english  washington
# 1  france        67.0            french       paris
# 2   japan       125.8          japanese       tokyo
# **********************************************************************************************************************

# Adding new Columns
df_country['Military_Budget'] = [3500, 1100, 600]  # military sector budget
df_country['Health_Budget'] = [1100, 300, 500]  # Health sector budget
df_country['Education_Budget'] = [700, 150, 250]  # Education sector budget

print("\nAfter added there columns:")
print(df_country)
# After added there columns:
#   Country  Population Official_Language     Capital  Military_Budget  Health_Budget  Education_Budget
# 0     usa       331.0           english  washington             3500           1100               700
# 1  france        67.0            french       paris             1100            300               150
# 2   japan       125.8          japanese       tokyo              600            500               250
# **********************************************************************************************************************

# Totals Across Rows - Calculate row-wise totals for the date columns

# Using Explicit Column Selection ([])
# Selects specific columns by name and sums row-wise
df_country["Total_Budget"] = df_country[
    ["Military_Budget", "Health_Budget", "Education_Budget"]].sum(axis=1)

#   Country  Population Official_Language     Capital  Military_Budget  Health_Budget  Education_Budget  Total_Budget
# 0     usa       331.0           english  washington             3500           1100               700          5300
# 1  france        67.0            french       paris             1100            300               150          1550
# 2   japan       125.8          japanese       tokyo              600            500               250          1350

# Using Direct Column Addition (+ Operator)
# Manually adds columns element-wise
df_country['Total_Budget'] = (
    df_country['Military_Budget'] +
    df_country['Health_Budget'] +
    df_country['Education_Budget'])

#   Country  Population Official_Language     Capital  Military_Budget  Health_Budget  Education_Budget  Total_Budget
# 0     usa       331.0           english  washington             3500           1100               700          5300
# 1  france        67.0            french       paris             1100            300               150          1550
# 2   japan       125.8          japanese       tokyo              600            500               250          1350

# Using .iloc[] for Positional Indexing
# 👉 Selects all columns from index 4 onward and sums row-wise
df_country["Total_Budget"] = df_country.iloc[:, 4:].sum(axis=1)

#   Country  Population Official_Language     Capital  Military_Budget  Health_Budget  Education_Budget  Total_Budget
# 0     usa       331.0           english  washington             3500           1100               700          5300
# 1  france        67.0            french       paris             1100            300               150          1550
# 2   japan       125.8          japanese       tokyo              600            500               250          1350

# Dynamic Approach - flexible way - assuming budget columns always have "Budget" in their name
df_country["Total_Budget"] = df_country.filter(like="Budget").sum(axis=1)

#   Country  Population Official_Language     Capital  Military_Budget  Health_Budget  Education_Budget  Total_Budget
# 0     usa       331.0           english  washington             3500           1100               700          5300
# 1  france        67.0            french       paris             1100            300               150          1550
# 2   japan       125.8          japanese       tokyo              600            500               250          1350


# Sum ALL Numeric Columns Dynamically - the budget columns plus Population
df_country["Total_Budget"] = df_country.select_dtypes(include='number').sum(axis=1)

#   Country  Population Official_Language     Capital  Military_Budget  Health_Budget  Education_Budget  Total_Budget
# 0     usa       331.0           english  washington             3500           1100               700        5631.0
# 1  france        67.0            french       paris             1100            300               150        1617.0
# 2   japan       125.8          japanese       tokyo              600            500               250        1475.8

# **********************************************************************************************************************

# casting
# astype(str) converts the column’s data type to a string (object)
df_country["Population"] = df_country["Population"].astype(str)

print(df_country.info())

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 3 entries, 0 to 2
# Data columns (total 8 columns):
#  #   Column             Non-Null Count  Dtype
# ---  ------             --------------  -----
#  0   Country            3 non-null      object
#  1   Population         3 non-null      object
#  2   Official_Language  3 non-null      object
#  3   Capital            3 non-null      object
#  4   Military_Budget    3 non-null      int64
#  5   Health_Budget      3 non-null      int64
#  6   Education_Budget   3 non-null      int64
#  7   Total_Budget       3 non-null      float64
# dtypes: float64(1), int64(3), object(4)
# **********************************************************************************************************************

# Splitting Strings in a Column - similar to "Text to Columns" feature in Excel
df_name = pd.DataFrame({'Full_Name': ['Mr_John_Doe', 'Ms_Jane_Smith', 'Dr_Alice_Jones']})

# Split into Title, First Name, and Last Name
df_name[['Title', 'First_Name', 'Last_Name']] = df_name['Full_Name'].str.split('_', expand=True)

print("\nUpdated DataFrame with Titles:")
print(df_name)
# Updated DataFrame with Titles:
#         Full_Name Title First_Name Last_Name
# 0     Mr_John_Doe    Mr       John       Doe
# **********************************************************************************************************************

# Bulk Parsing with DataFrames
# Parsing multiple custom dates in a DataFrame
dates = {'dates': ['29-Sep-2023', '5-Oct-2023', '15-Nov-2023']}
df_dates = pd.DataFrame(dates)
df_dates['parsed_dates'] = pd.to_datetime(df_dates['dates'], format='%d-%b-%Y')
print("\nParsed Dates DataFrame:")
print(df_dates)
# Parsed Dates DataFrame:
#          dates parsed_dates
# 0  29-Sep-2023   2023-09-29
# 1   5-Oct-2023   2023-10-05
# 2  15-Nov-2023   2023-11-15
# **********************************************************************************************************************


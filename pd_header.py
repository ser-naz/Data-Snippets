import pandas as pd

pd.options.display.width = 0

# Create DataFrame
df_country = pd.DataFrame({
    'Country': ['USA', 'France', 'Japan'],
    'Capital': ['Washington', 'Paris', 'Tokyo'],
    'Year Founded': [1776, 843, 660],
    'Population 2020': [331000000, 67000000, 125800000],
    'Population 2021': [332000000, 68000000, 126000000],
    'Male Female Ratio': [0.97, 0.95, 0.94]})

# **********************************************************************************************************************

# Display Column Names
print("Original Column Names:")
print(df_country.columns)
# Original Column Names:
# Index(['Country', 'Capital', 'Year Founded', 'Population 2020', 'Population 2021', 'Male Female Ratio'], dtype='object')
# **********************************************************************************************************************

# Remove Whitespace from Column Names
df_country.columns = df_country.columns.str.strip()
print("\nTrimmed Column Names:")
print(df_country.columns)

# **********************************************************************************************************************

# Standardize Column Names for Consistent Formatting
df_country.columns = df_country.columns.str.lower().str.replace(' ', '_')
print("\nStandardized Column Names:")
print(df_country)
# Standardized Column Names:
#   country     capital  year_founded  population_2020  population_2021  male_female_ratio
# 0     USA  Washington          1776        331000000        332000000               0.97
# 1  France       Paris           843         67000000         68000000               0.95
# 2   Japan       Tokyo           660        125800000        126000000               0.94
# **********************************************************************************************************************

# Rename Specific Columns
df_country = df_country.rename(columns={'male_female_ratio': 'gender_ratio'})
print("\nRenamed Columns:")
print(df_country)
# Renamed Columns:
#   country     capital  year_founded  population_2020  population_2021  gender_ratio
# 0     USA  Washington          1776        331000000        332000000          0.97
# 1  France       Paris           843         67000000         68000000          0.95
# 2   Japan       Tokyo           660        125800000        126000000          0.94
# **********************************************************************************************************************

# Reorder Columns
df_country = df_country[['country', 'year_founded', 'population_2020', 'population_2021', 'capital', 'gender_ratio']]
print("\nReordered Columns:")
print(df_country)
# Reordered Columns:
#   country  year_founded  population_2020  population_2021     capital  gender_ratio
# 0     USA          1776        331000000        332000000  Washington          0.97
# 1  France           843         67000000         68000000       Paris          0.95
# 2   Japan           660        125800000        126000000       Tokyo          0.94
# **********************************************************************************************************************

# Add Suffix to Column Names
df_country_2025 = df_country.add_suffix('_2025')
print("\nAdded Suffix to Column Names:")
print(df_country_2025)
# Added Suffix to Column Names:
#   country_2025  year_founded_2025  population_2020_2025  population_2021_2025 capital_2025  gender_ratio_2025
# 0          USA               1776             331000000             332000000   Washington               0.97
# 1       France                843              67000000              68000000        Paris               0.95
# 2        Japan                660             125800000             126000000        Tokyo               0.94
# **********************************************************************************************************************

# Add a Prefix '2025_' to All Column Names
df_2025_country = df_country.rename(columns=lambda x: f'2025_{x}')
print("\nDataFrame with Prefix '2025_':")
print(df_2025_country)
# DataFrame with Prefix '2025_':
#   2025_country  2025_year_founded  2025_population_2020  2025_population_2021 2025_capital  2025_gender_ratio
# 0          USA               1776             331000000             332000000   Washington               0.97
# 1       France                843              67000000              68000000        Paris               0.95
# 2        Japan                660             125800000             126000000        Tokyo               0.94
# **********************************************************************************************************************

# Select Columns by Partial Name - filter()
filtered_data = df_country.filter(like='population')
print("\nColumns Containing 'Population':")
print(filtered_data)
# Columns Containing 'Population':
#    population_2020  population_2021
# 0        331000000        332000000
# 1         67000000         68000000
# 2        125800000        126000000
# **********************************************************************************************************************

# Get a List of Column Names
column_names_v1 = df_country.columns.to_list()  # Preferred way
column_names_v2 = list(df_country.columns)
column_names_v3 = [col for col in df_country.columns]

print("\nList of Column Names:")
print(column_names_v1)
print(column_names_v2)
print(column_names_v3)
# List of Column Names:
# ['country', 'year_founded', 'population_2020', 'population_2021', 'capital', 'gender_ratio']
# ['country', 'year_founded', 'population_2020', 'population_2021', 'capital', 'gender_ratio']
# ['country', 'year_founded', 'population_2020', 'population_2021', 'capital', 'gender_ratio']
# **********************************************************************************************************************

# Create a new (empty) DataFrame using column names from an existing DataFrame.
columns = df_country.columns  # Extract column names from the original DataFrame
empty_df = pd.DataFrame(columns=columns)  # Create a new (empty) DataFrame with the same column names

# Print original and empty DataFrames
print("\nOriginal DataFrame:")
print(df_country)
print("\nEmpty DataFrame with Same Column Names:")
print(empty_df)
# Original DataFrame:
#   country  year_founded  population_2020  population_2021     capital  gender_ratio
# 0     USA          1776        331000000        332000000  Washington          0.97
# 1  France           843         67000000         68000000       Paris          0.95
# 2   Japan           660        125800000        126000000       Tokyo          0.94

# Empty DataFrame with Same Column Names:
# Empty DataFrame
# Columns: [country, year_founded, population_2020, population_2021, capital, gender_ratio]
# **********************************************************************************************************************

import re
# formating column names: 'OrderID' to 'order id'
# Create a DataFrame with DeliveryDateTime and fixed float values for OrderAmount
customers = {
    "OrderID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "CustomerName": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack"],
    "OrderDate": pd.date_range(start="2023-01-01", periods=10),
    "DeliveryDateTime": pd.date_range(start="2023-01-02 10:00:00", periods=10, freq="36h"),
    "OrderAmount": [150.25, 200.89, 50.34, 400.15, 300.75, 120.60, 180.45, 220.33, 90.18, 350.89],
    "Sex": ["Female", "Male", "Male", "Female", "Female", "Male", "Female", "Male", "Female", "Male"]}

df_customers = pd.DataFrame(customers)

#    OrderID CustomerName  OrderDate    DeliveryDateTime  OrderAmount     Sex
# 0      101        Alice 2023-01-01 2023-01-02 10:00:00       150.25  Female
# 1      102          Bob 2023-01-02 2023-01-03 22:00:00       200.89    Male

columns = df_customers.columns.to_list()
# ['OrderID', 'CustomerName', 'OrderDate', 'DeliveryDateTime', 'OrderAmount', 'Sex', 'OrderCategory']

# Function to convert column name to a more readable format
def format_column_name(name):
    # Use regular expression to insert space before each capital letter (except the first one)
    formatted_name = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', name).lower()
    return formatted_name

# Apply the formatting function to each column name
formatted_columns = [format_column_name(col) for col in columns]
# ['order id', 'customer name', 'order date', 'delivery date time', 'order amount', 'sex']

df_customers.columns = formatted_columns
print(df_customers)

#    order id customer name order date  delivery date time  order amount sex
# 0       101         Alice 2023-01-01 2023-01-02 10:00:00        150.25   F
# 1       102           Bob 2023-01-02 2023-01-03 22:00:00        200.89   M
# **********************************************************************************************************************

df_customers_sorted = df_customers.sort_index(axis=1, ascending=True)
print(df_customers_sorted)
#   customer name  delivery date time  order amount order date  order id     sex
# 0         Alice 2023-01-02 10:00:00        150.25 2023-01-01       101  Female
# 1           Bob 2023-01-03 22:00:00        200.89 2023-01-02       102    Male
# **********************************************************************************************************************

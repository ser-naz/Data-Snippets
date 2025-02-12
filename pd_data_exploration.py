import pandas as pd
import numpy as np

pd.set_option('future.no_silent_downcasting', True)
pd.options.display.width = 0
# **********************************************************************************************************************

data = {'id': [101, 102, 103, 'null', 105, 106, 107],
        'name': ['sam', 'zack', 'roy', 'diana', 'ross', 'nata', 'larry'],
        'rate': [21, 21, 19, 25, 34, 20, None],
        'type': ['W2', 'W2', 'W2', 'W2', 1099, 1099, 'NA'],
        'status': ['unknown', 'active', 'hold', 'active', 'active', 'hold', 'inactive'],
        'age': [21, 19, 33, np.nan, 34, 20, 45],
        'degree': [False, False, True, False, True, True, True],
        'birthday': ['Jan 3, 2004', '2006-01-09', '1992-10-01', '1989-01-01', '1991-03-01', '2005-01-12', '1980-11-01']}
df = pd.DataFrame(data)

print(df.head())
#      id   name  rate  type   status   age  degree     birthday
# 0   101    sam  21.0    W2  unknown  21.0   False  Jan 3, 2004
# 1   102   zack  21.0    W2   active  19.0   False   2006-01-09
# 2   103    roy  19.0    W2     hold  33.0    True   1992-10-01
# 3  null  diana  25.0    W2   active   NaN   False   1989-01-01
# 4   105   ross  34.0  1099   active  34.0    True   1991-03-01


# Number of rows
num_rows = df.shape[0] # gives the number of Rows in the DataFrame
rows = len(df)  # Same as df.shape[0]
# 7

# Number of columns
num_columns = df.shape[1] # gives the number of Columns in the DataFrame
#  8


print(df.shape)
# Output: (7, 8) 7 rows and 8 columns

print(df.info())

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 7 entries, 0 to 6
# Data columns (total 8 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   id        7 non-null      object
#  1   name      7 non-null      object
#  2   rate      6 non-null      float64
#  3   type      7 non-null      object
#  4   status    7 non-null      object
#  5   age       6 non-null      float64
#  6   degree    7 non-null      bool
#  7   birthday  7 non-null      object
# dtypes: bool(1), float64(2), object(5)
# memory usage: 527.0+ bytes

print(df.describe())

#             rate        age
# count   6.000000   6.000000
# mean   23.333333  28.666667
# std     5.609516  10.405127
# min    19.000000  19.000000
# 25%    20.250000  20.250000
# 50%    21.000000  27.000000
# 75%    24.000000  33.750000
# max    34.000000  45.000000

# Check unique values for each column
for column in df.columns:
    print(f"Unique values for '{column}':", df[column].unique().tolist())
    # print(df[column].value_counts()) # get how many time the value is presented
    print('------------------------')

# Output:
# Unique values for 'id': [101, 102, 103, 'null', 105, 106, 107]
# ------------------------
# Unique values for 'name': ['sam', 'zack', 'roy', 'diana', 'ross', 'nata', 'larry']
# ------------------------
# Unique values for 'rate': [21.0, 19.0, 25.0, 34.0, 20.0, nan]
# ------------------------
# Unique values for 'type': ['W2', 1099, 'NA']
# ------------------------
# Unique values for 'status': ['unknown', 'active', 'hold', 'inactive']
# ------------------------
# Unique values for 'age': [21.0, 19.0, 33.0, nan, 34.0, 20.0, 45.0]
# ------------------------
# Unique values for 'degree': [False, True]
# ------------------------
# Unique values for 'birthday': ['Jan 3, 2004', '2006-01-09', '1992-10-01', '1989-01-01', '1991-03-01', '2005-01-12', '1980-11-01']
# ------------------------

missing_values = ['null', 'NA', 'unknown']

# Replace the missing values with np.nan in the entire DataFrame
df.replace(missing_values, np.nan, inplace=True)

# Manually replace the specific 'Jan 3, 2004' with a consistent format
df['birthday'] = df['birthday'].replace('Jan 3, 2004', '2004-01-03')
# Overwrite the 'birthday' column for id 101 using at()
# df.at[0, 'birthday'] = '2004-01-03' # same result as df['birthday'].replace('Jan 3, 2004', '2004-01-03')

# Convert the 'birthday' column to datetime format
df['birthday'] = pd.to_datetime(df['birthday'])

print(df)

#     id   name  rate  type    status   age  degree   birthday
# 0  101    sam  21.0    W2       NaN  21.0   False 2004-01-03
# 1  102   zack  21.0    W2    active  19.0   False 2006-01-09
# 2  103    roy  19.0    W2      hold  33.0    True 1992-10-01
# 3  NaN  diana  25.0    W2    active   NaN   False 1989-01-01
# 4  105   ross  34.0  1099    active  34.0    True 1991-03-01
# 5  106   nata  20.0  1099      hold  20.0    True 2005-01-12
# 6  107  larry   NaN   NaN  inactive  45.0    True 1980-11-01

print(df.info())

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 7 entries, 0 to 6
# Data columns (total 8 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   id        6 non-null      object
#  1   name      7 non-null      object
#  2   rate      6 non-null      float64
#  3   type      6 non-null      object
#  4   status    6 non-null      object
#  5   age       6 non-null      float64
#  6   degree    7 non-null      bool
#  7   birthday  7 non-null      datetime64[ns]
# dtypes: bool(1), datetime64[ns](1), float64(2), object(4)

# Impute missing values for numeric columns (rate, age) with their mean
df['id'] = df['id'].fillna(df['id'].mean().astype(int))
df['age'] = df['age'].fillna(df['age'].mean()).astype(int)

# Impute missing values for categorical columns (status, type) with their mode
df['status'] = df['status'].fillna(df['status'].mode()[0])

#     id   name  rate  type    status  age  degree   birthday
# 0  101    sam  21.0    W2    active   21   False 2004-01-03
# 1  102   zack  21.0    W2    active   19   False 2006-01-09
# 2  103    roy  19.0    W2      hold   33    True 1992-10-01
# 3  104  diana  25.0    W2    active   28   False 1989-01-01
# 4  105   ross  34.0  1099    active   34    True 1991-03-01
# 5  106   nata  20.0  1099      hold   20    True 2005-01-12
# 6  107  larry   NaN   NaN  inactive   45    True 1980-11-01

# Get rows with NaN values
rows_with_nan = df[df.isna().any(axis=1)]
print(rows_with_nan)

#     id   name  rate type    status  age  degree   birthday
# 6  107  larry   NaN  NaN  inactive   45    True 1980-11-01

# at this point it's clear that the last row needs to drop because rate and type are unknown
df.dropna(inplace=True)

#     id   name  rate  type  status  age  degree   birthday
# 0  101    sam  21.0    W2  active   21   False 2004-01-03
# 1  102   zack  21.0    W2  active   19   False 2006-01-09
# 2  103    roy  19.0    W2    hold   33    True 1992-10-01
# 3  104  diana  25.0    W2  active   28   False 1989-01-01
# 4  105   ross  34.0  1099  active   34    True 1991-03-01
# 5  106   nata  20.0  1099    hold   20    True 2005-01-12
# **********************************************************************************************************************

# Create a DataFrame with countries, capitals, populations, male-female ratios, and languages
data = {
    'country': ['United States', 'Canada', 'USA', 'Mexico', 'Canada', 'UK', 'Germany', 'France', 'Germany', 'Germany'],
    'capital': ['Washington D.C.', 'Ottawa', 'Washington D.C.', 'Mexico City', 'Ottawa', 'London', 'Berlin', 'Paris',
                'Berlin', 'Berlin'],
    'population': [331, 38, 331, 128, 38, 67, 83, 67, 83, 83],
    'male_female_ratio': [1.01, None, 1.01, 1.05, 1.02, 1.01, 1.06, 1.00, 1.06, 1.06],
    'language': ['English', 'English/French', 'English', 'Spanish', 'English/French', 'English', 'German', 'French',
                 'German', 'German/Austrian']}

# Create the DataFrame
df_countries = pd.DataFrame(data)

# Show the structure and summary of the data
print(df_countries.info())

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10 entries, 0 to 9
# Data columns (total 5 columns):
#  #   Column             Non-Null Count  Dtype
# ---  ------             --------------  -----
#  0   country            10 non-null     object
#  1   capital            10 non-null     object
#  2   population         10 non-null     int64
#  3   male_female_ratio  9 non-null      float64
#  4   language           10 non-null     object
# dtypes: float64(1), int64(1), object(3)
# memory usage: 528.0+ bytes

print(df_countries.describe())  # Shows summary statistics for numeric columns

#        population  male_female_ratio
# count   10.000000           9.000000
# mean   124.900000           1.031111
# std    111.574041           0.025712
# min     38.000000           1.000000
# 25%     67.000000           1.010000
# 50%     83.000000           1.020000
# 75%    116.750000           1.060000
# max    331.000000           1.060000

# Create a dictionary of unique values and their counts for each column
unique_values_dict = {}
for column in df_countries.columns:
    unique_values_dict[column] = df_countries[column].value_counts().to_dict()

# Print unique values for each column
for k, v in unique_values_dict.items():
    print(k, v)  # Prints each column and its unique value counts

# country {'Germany': 3, 'Canada': 2, 'United States': 1, 'USA': 1, 'Mexico': 1, 'UK': 1, 'France': 1}
# capital {'Berlin': 3, 'Washington D.C.': 2, 'Ottawa': 2, 'Mexico City': 1, 'London': 1, 'Paris': 1}
# population {83: 3, 331: 2, 38: 2, 67: 2, 128: 1}
# male_female_ratio {1.01: 3, 1.06: 3, 1.05: 1, 1.02: 1, 1.0: 1}
# language {'English': 3, 'English/French': 2, 'German': 2, 'Spanish': 1, 'French': 1, 'German/Austrian': 1}

# Drop rows with duplicate values (the values in all columns must be the same)
df_countries.drop_duplicates(inplace=True)
print(df_countries)

#          country          capital  population  male_female_ratio         language
# 0  United States  Washington D.C.         331               1.01          English
# 1         Canada           Ottawa          38                NaN   English/French
# 2            USA  Washington D.C.         331               1.01          English
# 3         Mexico      Mexico City         128               1.05          Spanish
# 4         Canada           Ottawa          38               1.02   English/French
# 5             UK           London          67               1.01          English
# 6        Germany           Berlin          83               1.06           German
# 7         France            Paris          67               1.00           French
# 9        Germany           Berlin          83               1.06  German/Austrian

# Drop rows where the 'country' is 'USA'
df_countries = df_countries[df_countries['country'] != 'USA']  # Filters out rows where 'country' is 'USA'

# Drop rows with any missing values (NaN)
df_countries.dropna(inplace=True)
print(df_countries)

# 0  United States  Washington D.C.         331               1.01          English
# 3         Mexico      Mexico City         128               1.05          Spanish
# 4         Canada           Ottawa          38               1.02   English/French
# 5             UK           London          67               1.01          English
# 6        Germany           Berlin          83               1.06           German
# 7         France            Paris          67               1.00           French
# 9        Germany           Berlin          83               1.06  German/Austrian

# Drop duplicates based on the 'country' column, keeping the last occurrence
df_countries.drop_duplicates(subset='country', keep="last", inplace=True)
print(df_countries)

#          country          capital  population  male_female_ratio         language
# 0  United States  Washington D.C.         331               1.01          English
# 3         Mexico      Mexico City         128               1.05          Spanish
# 4         Canada           Ottawa          38               1.02   English/French
# 5             UK           London          67               1.01          English
# 7         France            Paris          67               1.00           French
# 9        Germany           Berlin          83               1.06  German/Austrian

# Replace a single value at once in the 'language' column
df_countries['language'] = df_countries['language'].replace({'Spanish': 'Spanish (MX)'})

print(df_countries)

#          country          capital  population  male_female_ratio         language
# 0  United States  Washington D.C.         331               1.01          English
# 3         Mexico      Mexico City         128               1.05     Spanish (MX)
# 4         Canada           Ottawa          38               1.02   English/French
# 5             UK           London          67               1.01          English
# 7         France            Paris          67               1.00           French
# 9        Germany           Berlin          83               1.06  German/Austrian

# Replace multiple values at once in the 'country' column
df_countries['country'] = df_countries['country'].replace(
    {'Mexico': 'Mexican Republic', 'France': 'Republic of France'})
# Replaces 'Mexico' with 'Mexican Republic' and 'France' with 'Republic of France'

print(df_countries)

#               country          capital  population  male_female_ratio         language
# 0       United States  Washington D.C.         331               1.01          English
# 3    Mexican Republic      Mexico City         128               1.05     Spanish (MX)
# 4              Canada           Ottawa          38               1.02   English/French
# 5                  UK           London          67               1.01          English
# 7  Republic of France            Paris          67               1.00           French
# 9             Germany           Berlin          83               1.06  German/Austrian

# Sort the DataFrame alphabetically by the 'country' column
df_countries.sort_values(by='country', ascending=True, inplace=True)
print(df_countries)

#               country          capital  population  male_female_ratio         language
# 4              Canada           Ottawa          38               1.02   English/French
# 9             Germany           Berlin          83               1.06  German/Austrian
# 3    Mexican Republic      Mexico City         128               1.05     Spanish (MX)
# 7  Republic of France            Paris          67               1.00           French
# 5                  UK           London          67               1.01          English
# 0       United States  Washington D.C.         331               1.01          English
# **********************************************************************************************************************

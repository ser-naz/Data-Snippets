import pandas as pd
from datetime import datetime
from datetime import timedelta

# NOW
# Get the current datetime using datetime
now_datetime = datetime.now()
now_datetime_str = now_datetime.strftime('%Y-%m-%d %H:%M:%S')
print(now_datetime, ' ', type(now_datetime))
# Output: 2025-01-26 15:15:16.317783   <class 'datetime.datetime'>

print(now_datetime_str, ' ', type(now_datetime_str))
# Output: 2025-01-26 15:15:16   <class 'str'>

# Get the current datetime using pd.to_datetime()
now_pd_to_datetime = pd.to_datetime("now")
print(now_pd_to_datetime, ' ', type(now_pd_to_datetime))
# Output: 2025-01-26 15:17:06.933815   <class 'pandas._libs.tslibs.timestamps.Timestamp'>

now_pd_to_datetime_str = now_pd_to_datetime.strftime('%Y-%m-%d %H:%M:%S')
print(now_pd_to_datetime_str, ' ', type(now_pd_to_datetime_str))
# Output: 2025-01-26 15:17:06   <class 'str'>
# **********************************************************************************************************************

# ASSIGNING DAY USING DATETIME from DATETIME
# create a sample date object by instantiating the date class and passing the y, m, and d as arguments.
sample_date1 = datetime(2023, 12, 10)
sample_date1_day_only = datetime(2023, 12, 10).date()
print(sample_date1, type(sample_date1))
# Output: 2023-12-10 00:00:00 <class 'datetime.datetime'>
print(sample_date1_day_only, type(sample_date1_day_only))
# Output: 2023-12-10 <class 'datetime.date'>


# ASSIGNING DAY USING PD.TO_DATETIME
# below line does the same without importing datetime (preferred). Both can be used to compare dates.
sample_date2 = pd.to_datetime("12/10/2023")
sample_date2_day_only = pd.to_datetime("12/10/2023").date()
print(sample_date2, type(sample_date2))
# Output: 2023-12-10 00:00:00 <class 'pandas._libs.tslibs.timestamps.Timestamp'>
print(sample_date2_day_only, type(sample_date2_day_only))
# Output: 2023-12-10 <class 'datetime.date'>

sample_date3 = pd.to_datetime("12-10-2023'")
sample_date3_day_only = pd.to_datetime("12-10-2023'").date()
print(sample_date3, type(sample_date3))
# Output: 2023-12-10 00:00:00 <class 'pandas._libs.tslibs.timestamps.Timestamp'>
print(sample_date3_day_only, type(sample_date3_day_only))
# Output: 2023-12-10 <class 'datetime.date'>

sample_date4 = pd.Timestamp('20231210')
sample_date4_day_only = pd.Timestamp('20231210').date()
print(sample_date4, type(sample_date4))
# Output: 2023-12-10 00:00:00 <class 'pandas._libs.tslibs.timestamps.Timestamp'>
print(sample_date4_day_only, type(sample_date4_day_only))
# Output: 2023-12-10 <class 'datetime.date'>
# **********************************************************************************************************************

# FINDING SPREAD
# day, hours, minutes, seconds spread between two points
start_point = pd.to_datetime('20230929') + pd.Timedelta(hours=20, minutes=15, seconds=00)
print(start_point)
end_point = pd.to_datetime('20230930') + pd.Timedelta(hours=8, minutes=30, seconds=00)
print(end_point)

worked_time = end_point - start_point
print(worked_time)
# Output: 0 days 12:15:00

# Convert worked time to hours (including minutes and seconds as decimals)
worked_hours = worked_time.total_seconds() / 3600  # 3600 seconds in an hour
print(worked_hours)
# Output: 12.25
# **********************************************************************************************************************

# TIMEDELTA FROM DATETIME MODULE
# timedelta IN PYTHON: from datetime import timedelta
delta_5_3_30_15 = timedelta(days=5, hours=3, minutes=30, seconds=15)
# You can also create timedelta objects with specific units like so:
delta_days = timedelta(days=7)
delta_hours = timedelta(hours=12)
delta_minutes = timedelta(minutes=35)
delta_seconds = timedelta(seconds=21)

# Combining timedelta objects
combined_delta_dt_7_12_35_21 = delta_days + delta_hours + delta_minutes + delta_seconds

print(delta_5_3_30_15)
# Output: 5 days, 3:30:15
print(combined_delta_dt_7_12_35_21)
# Output: 7 days, 12:35:21
print(combined_delta_dt_7_12_35_21 - delta_5_3_30_15)
# Output: 2 days, 9:05:06
# 7 days, 12:35:21 - 5 days, 3:30:15 = 2 days, 9:05:06

print(combined_delta_dt_7_12_35_21 == delta_5_3_30_15)  # False

# TIMEDELTA USING PD.TIMEDELTA
# pd.Timedelta() IN PANDAS. Creating a Timedelta object with a specified duration
delta_pd = pd.Timedelta(days=5, hours=3, minutes=30, seconds=15)
# You can also create Timedelta objects with specific units like so:
delta_days_pd = pd.Timedelta(days=7)
delta_hours_pd = pd.Timedelta(hours=12)
delta_minutes_pd = pd.Timedelta(minutes=35)
delta_seconds_pd = pd.Timedelta(seconds=21)

# Combining timedelta objects
combined_delta_pd = delta_days_pd + delta_hours_pd + delta_minutes_pd + delta_seconds_pd
print(combined_delta_pd - delta_pd)
# Output: 2 days 09:05:06
# **********************************************************************************************************************

# working with a data frame with datetime values
# Create a DataFrame
people = {'name': ['alice', 'john', 'robert'],
          'lucky_date': ['4-15-2022', '5-19-2022', '6-14-2022'],
          'dob': ['10/01/1999', '9/01/1962', '12/31/2012'],
          'hire_date': ['1999-10-11', '1962-02-25', '2012-5-8'],
          'date_off': [pd.Timestamp('20230929'), pd.Timestamp('20231126'), pd.Timestamp('20231125')]}
df = pd.DataFrame(people)

print(df)
#      name lucky_date         dob   hire_date   date_off
# 0   alice  4-15-2022  10/01/1999  1999-10-11 2023-09-29
# 1    john  5-19-2022   9/01/1962  1962-02-25 2023-11-26
# 2  robert  6-14-2022  12/31/2012    2012-5-8 2023-11-25

print('\n', df.dtypes)
#  name                  object
# lucky_date            object
# dob                   object
# hire_date             object
# date_off      datetime64[ns]
# dtype: object

# convert lucky date column to datetime format.
df['lucky_date'] = df['lucky_date'].apply(pd.to_datetime)

# below line does the same job (preferred). convert to datetime64[ns]
df['dob'] = pd.to_datetime(df['dob'])
df['hire_date'] = pd.to_datetime(df['hire_date'])

print('\n', df)
#       name lucky_date        dob  hire_date   date_off
# 0   alice 2022-04-15 1999-10-01 1999-10-11 2023-09-29
# 1    john 2022-05-19 1962-09-01 1962-02-25 2023-11-26
# 2  robert 2022-06-14 2012-12-31 2012-05-08 2023-11-25

print('\n', df.dtypes)
#  name                  object
# lucky_date    datetime64[ns]
# dob           datetime64[ns]
# hire_date     datetime64[ns]
# date_off      datetime64[ns]
# dtype: object

# finding day difference
df['spread'] =  df['lucky_date'] - df['hire_date']
print('\n', df)
#       name lucky_date        dob  hire_date   date_off     spread
# 0   alice 2022-04-15 1999-10-01 1999-10-11 2023-09-29  8222 days
# 1    john 2022-05-19 1962-09-01 1962-02-25 2023-11-26 21998 days
# 2  robert 2022-06-14 2012-12-31 2012-05-08 2023-11-25  3689 days
# **********************************************************************************************************************

# example with AM and PM
data = {'name': ['alice', 'john', 'robert'],
          'clock in': ['2023-09-29 8:30:00AM', '2023-09-29 10:00:00AM', '2023-09-29 3:30:00PM'],
          'clock out': ['2023-09-29 6:00:00 PM', '2023-09-29 5:00:00 PM', '2023-09-29 8:30:00 PM']}
df = pd.DataFrame(data)

df['clock in'] = pd.to_datetime(df['clock in'])
df['clock out'] = pd.to_datetime(df['clock out'])
df['worked time'] = df['clock out']  - df['clock in']
df['worked hours'] = df['worked time'].dt.total_seconds() / 3600

print(df)
#      name            clock in           clock out     worked time  worked hours
# 0   alice 2023-09-29 08:30:00 2023-09-29 18:00:00 0 days 09:30:00           9.5
# 1    john 2023-09-29 10:00:00 2023-09-29 17:00:00 0 days 07:00:00           7.0
# 2  robert 2023-09-29 15:30:00 2023-09-29 20:30:00 0 days 05:00:00           5.0
# **********************************************************************************************************************

# 24-hour into a 12-hour format
# converting the 24-hour into a 12-hour format with AM/PM notation using .strftime() method after creating the Timestamp
start_point = pd.to_datetime('20230929') + pd.Timedelta(hours=20, minutes=15, seconds=00)
print(start_point) # 2023-09-29 20:15:00

formatted_start_point = start_point.strftime('%Y-%m-%d %I:%M:%S %p')  # 12-hour format with AM/PM
print(formatted_start_point) # 2023-09-29 08:15:00 PM  <class 'str'>

end_point = pd.to_datetime('20230930') + pd.Timedelta(hours=8, minutes=30, seconds=00)
print(end_point) # 2023-09-30 08:30:00

formatted_end_point = end_point.strftime('%Y-%m-%d %I:%M:%S %p')  # 12-hour format with AM/PM
print(formatted_end_point) # 2023-09-30 08:30:00 AM  <class 'str'>
# **********************************************************************************************************************

# Adding Time Zones
import pytz

# Assign a timezone to a Timestamp
tz_aware_time = pd.to_datetime('2023-09-29 08:30:00').tz_localize('UTC')
print(tz_aware_time)  # Output: 2023-09-29 08:30:00+00:00

# Convert to another timezone
tz_converted_time = tz_aware_time.tz_convert('US/Eastern')
print(tz_converted_time)  # Output: 2023-09-29 04:30:00-04:00
# **********************************************************************************************************************

# Extracting Date/Time Components
# Extract components from a Timestamp
timestamp = pd.to_datetime('2023-09-29 20:15:00')
print(timestamp.year)   # Output: 2023
print(timestamp.month)  # Output: 9
print(timestamp.day)    # Output: 29
print(timestamp.hour)   # Output: 20
print(timestamp.minute) # Output: 15
print(timestamp.second) # Output: 0
# **********************************************************************************************************************

# Rounding and Floor/Ceiling Operations
# Rounding
rounded_time = pd.to_datetime('2023-09-29 08:37:45').round('30min')
print(rounded_time)  # Output: 2023-09-29 08:30:00

# Floor (truncate to the nearest interval)
floored_time = pd.to_datetime('2023-09-29 08:37:45').floor('30min')
print(floored_time)  # Output: 2023-09-29 08:30:00

# Ceiling (round up to the nearest interval)
ceiled_time = pd.to_datetime('2023-09-29 08:37:45').ceil('30min')
print(ceiled_time)  # Output: 2023-09-29 09:00:00
# **********************************************************************************************************************

# Working with Weekdays
# Get the day of the week
timestamp = pd.to_datetime('2023-09-29')  # This is a Friday
print(timestamp.day_name())  # Output: Friday
print(timestamp.weekday())   # Output: 4 (Monday=0, Sunday=6)

# Add days skipping weekends
workdays_only = timestamp + pd.offsets.BDay(3)
print(workdays_only)  # Output: 2023-10-04
# **********************************************************************************************************************

# Handling Missing or Invalid Dates
# Handling missing dates
dates = ['2023-09-29', None, 'Invalid date']
parsed_dates = pd.to_datetime(dates, errors='coerce')
print(parsed_dates)
# Output:
# DatetimeIndex(['2023-09-29', 'NaT', 'NaT'], dtype='datetime64[ns]', freq=None)
# **********************************************************************************************************************

# Generating Date Ranges
# Generate a date range
date_range = pd.date_range(start='2023-09-29', end='2023-10-05', freq='D')
print(date_range)
# Output: DatetimeIndex(['2023-09-29', '2023-09-30', '2023-10-01', ..., '2023-10-05'])

# Generate a range with specific frequency
hour_range = pd.date_range(start='2023-09-29 08:00:00', periods=5, freq='H')
print(hour_range)
# Output: DatetimeIndex(['2023-09-29 08:00:00', '2023-09-29 09:00:00', ..., '2023-09-29 12:00:00'])
# **********************************************************************************************************************

# CUSTOM DATE PARSING

# Parse a custom date format
custom_date = pd.to_datetime('29-Sep-2023 08:30:00', format='%d-%b-%Y %H:%M:%S')
print(custom_date)  # Output: 2023-09-29 08:30:00

# Day-Month-Year format with full month name
date1 = pd.to_datetime('29-September-2023', format='%d-%B-%Y')
print(date1)  # Output: 2023-09-29 00:00:00

# Day/Month/Year with 2-digit year
date2 = pd.to_datetime('29/09/23', format='%d/%m/%y')
print(date2)  # Output: 2023-09-29 00:00:00

# Month-Day-Year with hour and AM/PM
date3 = pd.to_datetime('09-29-2023 08:30 PM', format='%m-%d-%Y %I:%M %p')
print(date3)  # Output: 2023-09-29 20:30:00

# Dates without leading zeros
date4 = pd.to_datetime('9/5/2023', format='%m/%d/%Y')  # Single-digit month and day
print(date4)  # Output: 2023-09-05 00:00:00

# Dates with text components
date5 = pd.to_datetime('Today is 29-Sep-2023', format='Today is %d-%b-%Y')
print(date5)  # Output: 2023-09-29 00:00:00

# Parsing ISO-Like Formats
# Year-Month-Day with 'T' separating time
date6 = pd.to_datetime('2023-09-29T08:30:00', format='%Y-%m-%dT%H:%M:%S')
print(date6)  # Output: 2023-09-29 08:30:00

# Parsing Dates with Mixed Delimiters
date8 = pd.to_datetime('29.09.2023 08-30-00', format='%d.%m.%Y %H-%M-%S')
print(date8)  # Output: 2023-09-29 08:30:00


# Handling Quarter or Week Numbers
# Year and quarter
date9 = pd.to_datetime('2023-Q3', format='%Y-Q%q')
print(date9)  # Output: 2023-07-01 00:00:00 (start of Q3)
# Year and week number
date10 = pd.to_datetime('2023-W39', format='%Y-W%U')
print(date10)  # Output: 2023-09-25 00:00:00 (start of week 39)

# Resolve ambiguous Day-Month-Year format
date11 = pd.to_datetime('02-03-2023', format='%d-%m-%Y', dayfirst=True)
print(date11)  # Output: 2023-03-02 00:00:00

# Parsing Without Seconds
date12 = pd.to_datetime('2023-09-29 08:30', format='%Y-%m-%d %H:%M')
print(date12)  # Output: 2023-09-29 08:30:00

# Bulk Parsing with DataFrames
# Parsing multiple custom dates in a DataFrame
data = {'dates': ['29-Sep-2023', '5-Oct-2023', '15-Nov-2023']}
df = pd.DataFrame(data)
df['parsed_dates'] = pd.to_datetime(df['dates'], format='%d-%b-%Y')
print(df)
# Output:
#         dates parsed_dates
# 0  29-Sep-2023  2023-09-29
# 1   5-Oct-2023  2023-10-05
# 2  15-Nov-2023  2023-11-15


# an Excel file named 'example.xlsx' with a column 'date_column'
# Tells pandas to interpret the values in date_column as dates and automatically convert them to datetime64[ns].
# Pandas will handle the parsing for most standard date formats, including YYYY-MM-DD, MM/DD/YYYY, etc.

# Read the Excel file and parse the 'date_column' as datetime
df = pd.read_excel('example.xlsx', parse_dates=['date_column'])
# Multiple Date Columns
df1 = pd.read_excel('example.xlsx', parse_dates=['start_date', 'end_date'])


# Handling Custom Formats. Custom parsing function
custom_parser = lambda x: pd.to_datetime(x, format='%d-%b-%Y')
# Apply custom parser
df2 = pd.read_excel('example.xlsx', parse_dates=['date_column'], date_parser=custom_parser)
# **********************************************************************************************************************

# Duration in Weeks, Months, or Years
# Calculate duration in weeks
start = pd.to_datetime('2023-01-01')
end = pd.to_datetime('2023-12-31')
weeks = (end - start).days / 7
print(weeks)  # Output: 52.142857...

# Calculate approximate duration in months/years using relativedelta
from dateutil.relativedelta import relativedelta

months = relativedelta(end, start).months + relativedelta(end, start).years * 12
print(months)  # Output: 12

years = relativedelta(end, start).years
print(years)  # Output: 1
# **********************************************************************************************************************






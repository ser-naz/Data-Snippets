import pandas as pd
pd.options.display.width = 0

# **********************************************************************************************************************
"""
This project solves the issue of overpayment in home care payroll, which occurs when caregivers working 
with multiple patients at the same time (mutually shared shifts) aren’t properly paid for their hours.
The system should divide the caregiver’s hours by 2 for payroll purposes while keeping 
the pay rate unchanged (due to minimum wage laws). When the system doesn’t divide the hours correctly, 
it results in overpayment, where caregivers are paid double than they actually worked. 
This project identifies these discrepancies, flags them for correction, and the output shows ZEROS for 
the flagged instances, indicating potential overpayment.
"""
# **********************************************************************************************************************

payroll_data = {
    'employee id': [101, 101, 101, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102],
    'employee name': ['jacob', 'jacob', 'jacob', 'john', 'john', 'john', 'john', 'john', 'john', 'john', 'john', 'john',
                      'john', 'john', 'john', 'john', 'john'],
    'work date': ['2025-09-26', '2025-09-27', '2025-09-28', '2025-09-27', '2025-09-27', '2025-09-27', '2025-09-28',
                  '2025-09-28', '2025-09-29', '2025-09-29', '2025-09-29', '2025-09-30', '2025-10-01', '2025-10-01',
                  '2025-10-01', '2025-10-01', '2025-10-01'],
    'patient id': [77889, 77889, 77889, 55449, 55449, 80596, 55449, 80596, 55449, 55449, 80596, 80596, 80596, 80596,
                   55449, 55449, 55449],
    'pay code': ['regular', 'regular', 'regular', 'regular', 'regular', 'regular', 'regular', 'regular', 'regular',
                 'regular', 'regular', 'regular', 'regular', 'over time', 'regular', 'over time', 'over time'],
    'pay rate': [19.1, 19.1, 19.1, 19.1, 19.1, 19.1, 19.1, 19.1, 19.1, 19.1, 19.1, 19.1, 19.1, 28.65, 19.1, 28.65,
                 28.65],
    'hours worked': [4.0, 4.0, 4.0, 5.0, 1.5, 1.5, 4.0, 4.0, 1.0, 4.5, 4.5, 10.0, 2.0, 3.0, 2.0, 3.0, 2.5],
    'clock in': ['2025-09-26 09:00:00', '2025-09-27 09:00:00', '2025-09-28 09:00:00', '2025-09-27 11:00:00',
                 '2025-09-27 07:00:00', '2025-09-27 07:05:00', '2025-09-28 14:00:00', '2025-09-28 14:00:00',
                 '2025-09-29 08:00:00', '2025-09-29 10:00:00', '2025-09-29 10:00:00', '2025-09-30 08:00:00',
                 '2025-10-01 08:00:00', '2025-10-01 08:00:00', '2025-10-01 08:00:00', '2025-10-01 08:00:00',
                 '2025-10-01 05:00:00'],
    'clock out': ['2025-09-26 13:00:00', '2025-09-27 13:00:00', '2025-09-28 13:00:00', '2025-09-27 16:00:00',
                  '2025-09-27 10:00:00', '2025-09-27 10:05:00', '2025-09-28 18:00:00', '2025-09-28 18:00:00',
                  '2025-09-29 09:00:00', '2025-09-29 14:30:00', '2025-09-29 14:30:00', '2025-09-29 18:00:00',
                  '2025-10-01 18:00:00', '2025-10-01 18:00:00', '2025-10-01 18:00:00', '2025-10-01 18:00:00',
                  '2025-10-01 07:36:00']
}

df = pd.DataFrame(payroll_data)

# Convert 'clock in' and 'clock out' to datetime
df['clock in'] = pd.to_datetime(df['clock in'])
df['clock out'] = pd.to_datetime(df['clock out'])

# Sort the DataFrame by employee id, work date, patient id, and clock in
df_sorted = df.sort_values(by=['employee id', 'work date', 'patient id', 'clock in'])
# Initialize the 'Overlap' column with False
df['Over lap'] = False


# Function to check for overlaps
def find_overlaps(group, min_over_minutes=15):
    overlaps = []
    # Compare each pair of shifts in the group
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            shift1 = group.iloc[i]
            shift2 = group.iloc[j]

            # calculate overlap window
            latest_start = max(shift1['clock in'], shift2['clock in'])
            earliest_end = min(shift1['clock out'], shift2['clock out'])

            # calculate duration of overlap in minutes
            overlap_duration = (earliest_end - latest_start).total_seconds() / 60

            if overlap_duration >= min_over_minutes:
                if shift1['patient id'] != shift2['patient id']:
                    overlaps.append((shift1.name, shift2.name))

    return overlaps


# Group by employee id and work date
grouped = df_sorted.groupby(['employee id', 'work date'])
# Iterate over each group and find overlaps
for (emp_id, work_date), group in grouped:
    overlaps = find_overlaps(group)
    for idx1, idx2 in overlaps:
        # Mark overlap as True in the 'Overlap' column for both shifts
        df.at[idx1, 'Over lap'] = True
        df.at[idx2, 'Over lap'] = True

# Exclude the rows where 'Overlap' is False
df_with_overlaps = df[df['Over lap'] == True]
# Ensure df_with_overlaps is a copy of the filtered DataFrame to avoid the warning
df_with_overlaps = df_with_overlaps.copy()

df_final = df_with_overlaps[
    ['employee id', 'employee name', 'work date', 'patient id', 'hours worked', 'clock in', 'clock out']]

df_final = df_final.groupby(['employee id', 'employee name', 'work date', 'patient id'], as_index=False).agg(
    {'hours worked': 'sum',  # Sum hours worked for each group
     'clock in': 'first',  # Take the first clock in (assuming same shift)
     'clock out': 'last'})

# add the "Actual hours" column
df_final['Actual hours'] = (df_final['clock out'] - df_final['clock in']).dt.total_seconds() / 3600

# this must be checked. Zero means that the hours were not divided by 2.
df_final['Check This'] = df_final['Actual hours'] - df_final['hours worked']

print(df_final)


# output:
#    employee id employee name   work date  patient id  hours worked            clock in           clock out  Actual hours  Check This
# 0          102          john  2025-09-27       55449           1.5 2025-09-27 07:00:00 2025-09-27 10:00:00           3.0         1.5
# 1          102          john  2025-09-27       80596           1.5 2025-09-27 07:05:00 2025-09-27 10:05:00           3.0         1.5
# 2          102          john  2025-09-28       55449           4.0 2025-09-28 14:00:00 2025-09-28 18:00:00           4.0         0.0 # over payment - must be fixed
# 3          102          john  2025-09-28       80596           4.0 2025-09-28 14:00:00 2025-09-28 18:00:00           4.0         0.0 # over payment - must be fixed
# 4          102          john  2025-09-29       55449           4.5 2025-09-29 10:00:00 2025-09-29 14:30:00           4.5         0.0 # over payment - must be fixed
# 5          102          john  2025-09-29       80596           4.5 2025-09-29 10:00:00 2025-09-29 14:30:00           4.5         0.0 # over payment - must be fixed
# 6          102          john  2025-10-01       55449           5.0 2025-10-01 08:00:00 2025-10-01 18:00:00          10.0         5.0
# 7          102          john  2025-10-01       80596           5.0 2025-10-01 08:00:00 2025-10-01 18:00:00          10.0         5.0


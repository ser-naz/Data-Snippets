import pandas as pd

pd.options.display.width = 0

# Use apply() when:
#     You need to apply a function across rows or columns.
#     You are working with a DataFrame or Series and need to avoid explicit loops for better performance and readability.
#     You can express the logic in a single function or lambda.

# Use loops when:
#     You need more control over the iteration process, especially with complex or nested logic.
#     The task involves more than just applying a function, such as making complex updates to the DataFrame or interacting with external data.
#     You need to handle side effects or modify the DataFrame directly during iteration.


# Create a DataFrame with DeliveryDateTime and fixed float values for OrderAmount
data = {
    "OrderID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "FirstName": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack"],
    "LastName": ["Tank", "Lee", "John", "Luis", "Ives", "Woo", "Chill", "Tommy", "Naz", "Zack"],
    "OrderDate": pd.date_range(start="2023-01-01", periods=10),
    "DeliveryDateTime": pd.date_range(start="2023-01-02 10:00:00", periods=10, freq="36h"),
    "OrderAmount": [150.25, 200.89, 50.34, 400.15, 300.75, 120.60, 180.45, 220.33, 90.18, 350.89],
    "Sex": ["Female", "Male", "Male", "Female", "Female", "Male", "Female", "Male", "Female", "Male"]}

df = pd.DataFrame(data)

#    OrderID FirstName LastName  OrderDate    DeliveryDateTime  OrderAmount     Sex
# 0      101     Alice     Tank 2023-01-01 2023-01-02 10:00:00       150.25  Female
# 1      102       Bob      Lee 2023-01-02 2023-01-03 22:00:00       200.89    Male
# 2      103   Charlie     John 2023-01-03 2023-01-05 10:00:00        50.34    Male
# 3      104     Diana     Luis 2023-01-04 2023-01-06 22:00:00       400.15  Female
# 4      105       Eve     Ives 2023-01-05 2023-01-08 10:00:00       300.75  Female
# 5      106     Frank      Woo 2023-01-06 2023-01-09 22:00:00       120.60    Male
# 6      107     Grace    Chill 2023-01-07 2023-01-11 10:00:00       180.45  Female
# 7      108      Hank    Tommy 2023-01-08 2023-01-12 22:00:00       220.33    Male
# 8      109       Ivy      Naz 2023-01-09 2023-01-14 10:00:00        90.18  Female
# 9      110      Jack     Zack 2023-01-10 2023-01-15 22:00:00       350.89    Male

# mapping sex column values "Female": 'F', "Male": 'M'
df['Sex'] = df['Sex'].map({"Female": 'F', "Male": 'M'})

#    OrderID FirstName LastName  OrderDate    DeliveryDateTime  OrderAmount Sex
# 0      101     Alice     Tank 2023-01-01 2023-01-02 10:00:00       150.25   F
# 1      102       Bob      Lee 2023-01-02 2023-01-03 22:00:00       200.89   M
# 2      103   Charlie     John 2023-01-03 2023-01-05 10:00:00        50.34   M
# 3      104     Diana     Luis 2023-01-04 2023-01-06 22:00:00       400.15   F
# 4      105       Eve     Ives 2023-01-05 2023-01-08 10:00:00       300.75   F
# 5      106     Frank      Woo 2023-01-06 2023-01-09 22:00:00       120.60   M
# 6      107     Grace    Chill 2023-01-07 2023-01-11 10:00:00       180.45   F
# 7      108      Hank    Tommy 2023-01-08 2023-01-12 22:00:00       220.33   M
# 8      109       Ivy      Naz 2023-01-09 2023-01-14 10:00:00        90.18   F
# 9      110      Jack     Zack 2023-01-10 2023-01-15 22:00:00       350.89   M

# "Low": If OrderAmount is less than 100.
# "Medium": If OrderAmount is between 100 and 300 (inclusive).
# "High": If OrderAmount is greater than 300.

# Define the function to categorize OrderAmount
def categorize_order_amount(amount):
    if amount < 100:
        return "Low"
    elif 100 <= amount <= 300:
        return "Medium"
    else:
        return "High"

# Apply the function using apply()
df['OrderCategory'] = df['OrderAmount'].apply(categorize_order_amount)

#    OrderID FirstName LastName  OrderDate    DeliveryDateTime  OrderAmount Sex OrderCategory
# 0      101     Alice     Tank 2023-01-01 2023-01-02 10:00:00       150.25   F        Medium
# 1      102       Bob      Lee 2023-01-02 2023-01-03 22:00:00       200.89   M        Medium
# 2      103   Charlie     John 2023-01-03 2023-01-05 10:00:00        50.34   M           Low
# 3      104     Diana     Luis 2023-01-04 2023-01-06 22:00:00       400.15   F          High
# 4      105       Eve     Ives 2023-01-05 2023-01-08 10:00:00       300.75   F          High
# 5      106     Frank      Woo 2023-01-06 2023-01-09 22:00:00       120.60   M        Medium
# 6      107     Grace    Chill 2023-01-07 2023-01-11 10:00:00       180.45   F        Medium
# 7      108      Hank    Tommy 2023-01-08 2023-01-12 22:00:00       220.33   M        Medium
# 8      109       Ivy      Naz 2023-01-09 2023-01-14 10:00:00        90.18   F           Low
# 9      110      Jack     Zack 2023-01-10 2023-01-15 22:00:00       350.89   M          High


# Function to calculate the delivery delay
def calculate_delivery_delay(row):
    delay = (row['DeliveryDateTime'] - row['OrderDate']).days
    return delay

# Apply the function to calculate the delivery delay for each order
df['DeliveryDelay'] = df.apply(calculate_delivery_delay, axis=1)

df['DeliveryTime'] = df['DeliveryDateTime'].apply(lambda x: x.strftime('%H:%M'))

#    OrderID FirstName LastName  OrderDate    DeliveryDateTime  OrderAmount Sex OrderCategory  DeliveryDelay DeliveryTime
# 0      101     Alice     Tank 2023-01-01 2023-01-02 10:00:00       150.25   F        Medium              1        10:00
# 1      102       Bob      Lee 2023-01-02 2023-01-03 22:00:00       200.89   M        Medium              1        22:00
# 2      103   Charlie     John 2023-01-03 2023-01-05 10:00:00        50.34   M           Low              2        10:00
# 3      104     Diana     Luis 2023-01-04 2023-01-06 22:00:00       400.15   F          High              2        22:00
# 4      105       Eve     Ives 2023-01-05 2023-01-08 10:00:00       300.75   F          High              3        10:00
# 5      106     Frank      Woo 2023-01-06 2023-01-09 22:00:00       120.60   M        Medium              3        22:00
# 6      107     Grace    Chill 2023-01-07 2023-01-11 10:00:00       180.45   F        Medium              4        10:00
# 7      108      Hank    Tommy 2023-01-08 2023-01-12 22:00:00       220.33   M        Medium              4        22:00
# 8      109       Ivy      Naz 2023-01-09 2023-01-14 10:00:00        90.18   F           Low              5        10:00
# 9      110      Jack     Zack 2023-01-10 2023-01-15 22:00:00       350.89   M          High              5        22:00

df['FistInitial'] = df['LastName'].apply(lambda x: x[0:1])

#    OrderID FirstName LastName  OrderDate    DeliveryDateTime  OrderAmount Sex OrderCategory  DeliveryDelay DeliveryTime FistInitial
# 0      101     Alice     Tank 2023-01-01 2023-01-02 10:00:00       150.25   F        Medium              1        10:00           T
# 1      102       Bob      Lee 2023-01-02 2023-01-03 22:00:00       200.89   M        Medium              1        22:00           L
# 2      103   Charlie     John 2023-01-03 2023-01-05 10:00:00        50.34   M           Low              2        10:00           J
# 3      104     Diana     Luis 2023-01-04 2023-01-06 22:00:00       400.15   F          High              2        22:00           L
# 4      105       Eve     Ives 2023-01-05 2023-01-08 10:00:00       300.75   F          High              3        10:00           I
# 5      106     Frank      Woo 2023-01-06 2023-01-09 22:00:00       120.60   M        Medium              3        22:00           W
# 6      107     Grace    Chill 2023-01-07 2023-01-11 10:00:00       180.45   F        Medium              4        10:00           C
# 7      108      Hank    Tommy 2023-01-08 2023-01-12 22:00:00       220.33   M        Medium              4        22:00           T
# 8      109       Ivy      Naz 2023-01-09 2023-01-14 10:00:00        90.18   F           Low              5        10:00           N
# 9      110      Jack     Zack 2023-01-10 2023-01-15 22:00:00       350.89   M          High              5        22:00           Z


# Text Transformation
df['OrderCategory'] = df['OrderCategory'].apply(lambda x: x.lower())

#    OrderID FirstName LastName  OrderDate    DeliveryDateTime  OrderAmount Sex OrderCategory  DeliveryDelay DeliveryTime FistInitial
# 0      101     Alice     Tank 2023-01-01 2023-01-02 10:00:00       150.25   F        medium              1        10:00           T
# 1      102       Bob      Lee 2023-01-02 2023-01-03 22:00:00       200.89   M        medium              1        22:00           L
# 2      103   Charlie     John 2023-01-03 2023-01-05 10:00:00        50.34   M           low              2        10:00           J
# 3      104     Diana     Luis 2023-01-04 2023-01-06 22:00:00       400.15   F          high              2        22:00           L
# 4      105       Eve     Ives 2023-01-05 2023-01-08 10:00:00       300.75   F          high              3        10:00           I
# 5      106     Frank      Woo 2023-01-06 2023-01-09 22:00:00       120.60   M        medium              3        22:00           W
# 6      107     Grace    Chill 2023-01-07 2023-01-11 10:00:00       180.45   F        medium              4        10:00           C
# 7      108      Hank    Tommy 2023-01-08 2023-01-12 22:00:00       220.33   M        medium              4        22:00           T
# 8      109       Ivy      Naz 2023-01-09 2023-01-14 10:00:00        90.18   F           low              5        10:00           N
# 9      110      Jack     Zack 2023-01-10 2023-01-15 22:00:00       350.89   M          high              5        22:00           Z

# Combining Multiple Columns
def calculate_discount(row):
    if row['OrderAmount'] > 200 and row['DeliveryDelay'] > 3:
        return 0.1 * row['OrderAmount']  # 10% discount
    return 0

df['Discount'] = df.apply(calculate_discount, axis=1)

#    OrderID FirstName LastName  OrderDate    DeliveryDateTime  OrderAmount Sex OrderCategory  DeliveryDelay DeliveryTime FistInitial  Discount
# 0      101     Alice     Tank 2023-01-01 2023-01-02 10:00:00       150.25   F        medium              1        10:00           T     0.000
# 1      102       Bob      Lee 2023-01-02 2023-01-03 22:00:00       200.89   M        medium              1        22:00           L     0.000
# 2      103   Charlie     John 2023-01-03 2023-01-05 10:00:00        50.34   M           low              2        10:00           J     0.000
# 3      104     Diana     Luis 2023-01-04 2023-01-06 22:00:00       400.15   F          high              2        22:00           L     0.000
# 4      105       Eve     Ives 2023-01-05 2023-01-08 10:00:00       300.75   F          high              3        10:00           I     0.000
# 5      106     Frank      Woo 2023-01-06 2023-01-09 22:00:00       120.60   M        medium              3        22:00           W     0.000
# 6      107     Grace    Chill 2023-01-07 2023-01-11 10:00:00       180.45   F        medium              4        10:00           C     0.000
# 7      108      Hank    Tommy 2023-01-08 2023-01-12 22:00:00       220.33   M        medium              4        22:00           T    22.033
# 8      109       Ivy      Naz 2023-01-09 2023-01-14 10:00:00        90.18   F           low              5        10:00           N     0.000
# 9      110      Jack     Zack 2023-01-10 2023-01-15 22:00:00       350.89   M          high              5        22:00           Z    35.089

# Transforming Data Across Multiple Columns (Multiple Column Arguments)
def high_amount_alert(row):
    if row['OrderCategory'] == 'high' and row['DeliveryDelay'] >= 3:
        return "Late order"
    return "Normal"

df['Alert'] = df.apply(high_amount_alert, axis=1)

#    OrderID FirstName LastName  OrderDate    DeliveryDateTime  OrderAmount Sex OrderCategory  DeliveryDelay DeliveryTime FistInitial  Discount       Alert
# 0      101     Alice     Tank 2023-01-01 2023-01-02 10:00:00       150.25   F        medium              1        10:00           T     0.000      Normal
# 1      102       Bob      Lee 2023-01-02 2023-01-03 22:00:00       200.89   M        medium              1        22:00           L     0.000      Normal
# 2      103   Charlie     John 2023-01-03 2023-01-05 10:00:00        50.34   M           low              2        10:00           J     0.000      Normal
# 3      104     Diana     Luis 2023-01-04 2023-01-06 22:00:00       400.15   F          high              2        22:00           L     0.000      Normal
# 4      105       Eve     Ives 2023-01-05 2023-01-08 10:00:00       300.75   F          high              3        10:00           I     0.000  Late order
# 5      106     Frank      Woo 2023-01-06 2023-01-09 22:00:00       120.60   M        medium              3        22:00           W     0.000      Normal
# 6      107     Grace    Chill 2023-01-07 2023-01-11 10:00:00       180.45   F        medium              4        10:00           C     0.000      Normal
# 7      108      Hank    Tommy 2023-01-08 2023-01-12 22:00:00       220.33   M        medium              4        22:00           T    22.033      Normal
# 8      109       Ivy      Naz 2023-01-09 2023-01-14 10:00:00        90.18   F           low              5        10:00           N     0.000      Normal
# 9      110      Jack     Zack 2023-01-10 2023-01-15 22:00:00       350.89   M          high              5        22:00           Z    35.089  Late order
# **********************************************************************************************************************

# LOOPING
# index + loc vs iterrows() + df.at
# For a large DataFrame (e.g., 10,000 rows) - iterrows() + df.at: ~10x slower (or more) than df.index + df.loc

for i in df.index:
    if df.loc[i, 'OrderAmount'] > 100 and df.loc[i, 'DeliveryDelay'] < 2:
        df.loc[i, 'SpecialStatus'] = 'VIP'
    else:
        df.loc[i, 'SpecialStatus'] = 'Standard'

# SAME RESULT
for index, row in df.iterrows():
    if row['OrderAmount'] > 100 and row['DeliveryDelay'] < 2:
        df.at[index, 'SpecialStatus'] = 'VIP'
    else:
        df.at[index, 'SpecialStatus'] = 'Standard'

#    OrderID FirstName LastName  OrderDate    DeliveryDateTime  OrderAmount Sex OrderCategory  DeliveryDelay DeliveryTime FistInitial  Discount       Alert SpecialStatus
# 0      101     Alice     Tank 2023-01-01 2023-01-02 10:00:00       150.25   F        medium              1        10:00           T     0.000      Normal           VIP
# 1      102       Bob      Lee 2023-01-02 2023-01-03 22:00:00       200.89   M        medium              1        22:00           L     0.000      Normal           VIP
# 2      103   Charlie     John 2023-01-03 2023-01-05 10:00:00        50.34   M           low              2        10:00           J     0.000      Normal      Standard
# 3      104     Diana     Luis 2023-01-04 2023-01-06 22:00:00       400.15   F          high              2        22:00           L     0.000      Normal      Standard
# 4      105       Eve     Ives 2023-01-05 2023-01-08 10:00:00       300.75   F          high              3        10:00           I     0.000  Late order      Standard
# 5      106     Frank      Woo 2023-01-06 2023-01-09 22:00:00       120.60   M        medium              3        22:00           W     0.000      Normal      Standard
# 6      107     Grace    Chill 2023-01-07 2023-01-11 10:00:00       180.45   F        medium              4        10:00           C     0.000      Normal      Standard
# 7      108      Hank    Tommy 2023-01-08 2023-01-12 22:00:00       220.33   M        medium              4        22:00           T    22.033      Normal      Standard
# 8      109       Ivy      Naz 2023-01-09 2023-01-14 10:00:00        90.18   F           low              5        10:00           N     0.000      Normal      Standard
# 9      110      Jack     Zack 2023-01-10 2023-01-15 22:00:00       350.89   M          high              5        22:00           Z    35.089  Late order      Standard

# Nested Iteration (Multi-level Loops):

data = {
    'OrderID': [101, 102, 103],
    'CustomerName': ['Alice', 'Bob', 'Charlie'],
    'Items': [
        [{"item": "Laptop", "price": 1000}, {"item": "Mouse", "price": 50}],
        [{"item": "Phone", "price": 500}, {"item": "Charger", "price": 20}],
        [{"item": "Tablet", "price": 300}, {"item": "Keyboard", "price": 80}]]}

df = pd.DataFrame(data)

# Function to apply discount to items
def apply_discount(item):
    if item['price'] > 100:
        item['discount'] = item['price'] * 0.1
    else:
        item['discount'] = item['price'] * 0.05
    return item

# Nested iteration: Loop through each row (order) and then each item within the order
for index, row in df.iterrows():
    # Loop through each item in the 'Items' list
    for item in row['Items']:
        # Apply discount to each item
        item = apply_discount(item)
        # Update the item dictionary with the discount (or you can modify the DataFrame directly)
        row['Items'][row['Items'].index(item)] = item
# **********************************************************************************************************************



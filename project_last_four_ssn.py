import unicodedata
import re
import pandas as pd
from rapidfuzz import fuzz, process

pd.options.display.width = 0

# **********************************************************************************************************************
"""
Record Matching Using Last 4 Digits of SSN and Fuzzy Name Matching

This project matches records from two datasets:
df_a: Contains the last four digits of SSNs and associated names.
df_b: Contains full SSNs and names.

The goal is to accurately match records by combining:
The last four digits of SSN (from both datasets)
Fuzzy name matching to account for variations or discrepancies in name formatting (e.g., misspellings).

This solution automates the matching process, enabling reconciliation and merging of data even when full SSNs or 
names don't perfectly align across datasets.
"""
# **********************************************************************************************************************


# Sample dataset (df_a) with last 4 digits of SSNs and names
df_a = pd.DataFrame({
    'ssn': [2334, 2334, 1235, 4567],
    'name': ['ana dow', 'an dee', 'anna smit', 'any rod'],
    'amount': [1500, 235.36, 965.25, 50.1]
})

# Sample dataset (df_b) with full SSNs and names
df_b = pd.DataFrame({
    'ssn': ['234-09-2334', '321-76-1235', '890-87-4567', '123-45-8765', '098-77-2334'],
    'name': ['anna dee', 'anna smit', 'anna rod', 'ser naz', 'ana dew'],
    'id': [101, 102, 103, 104, 105]
})

# Create a new column 'last4' in df_b which contains the last 4 digits of the SSN for easier matching
df_b['last4'] = df_b['ssn'].str[-4:].astype(int)

# Function to normalize text by converting it to uppercase and removing non-alphanumeric characters
def normalize_text(text):
    if pd.isna(text):
        return ""  # Handle NaN values gracefully
    text = unicodedata.normalize('NFKD', str(text))  # Normalize Unicode characters
    text = "".join(c for c in text if not unicodedata.combining(c))  # Remove diacritics
    text = re.sub(r"[^A-Z0-9]", "", text.upper())  # Remove non-alphanumeric characters and convert to uppercase
    return text

# List to store the matches
matches = []

# Iterate over each row in df_a (the dataset with last 4 SSNs)
for i, row_a in df_a.iterrows():
    last4 = row_a['ssn']  # Extract the last 4 digits of SSN from df_a
    name_a = row_a['name']  # Extract the name from df_a

    # Filter df_b for records with matching last4 SSNs
    subset_b = df_b[df_b['last4'] == last4]

    if len(subset_b) == 0:
        # No possible match found for this record
        match_dict = {'index': i, 'score': 0}  # No match, so score is 0
        for col in df_b.columns:
            match_dict[col] = None  # Add None values for the columns from df_b
        matches.append(match_dict)  # Append the result to the matches list

    elif len(subset_b) == 1:
        # Only one possible match, so take it directly
        match_row = subset_b.iloc[0].to_dict()  # Convert the matched row from df_b to a dictionary
        match_row.update({'index': i, 'score': 100})  # Update with the index and a perfect match score (100)
        matches.append(match_row)  # Append the result to the matches list

    else:
        # Multiple candidates found, need to use fuzzy name matching
        best_match = process.extractOne(name_a, subset_b['name'], scorer=fuzz.ratio)  # Find best fuzzy match for name
        best_name = best_match[0]  # Extract the best matching name
        best_score = best_match[1]  # Extract the matching score
        best_row = subset_b[subset_b['name'] == best_name].iloc[0].to_dict()  # Get the full record of the best match
        best_row.update({'index': i, 'score': best_score})  # Add the index and score to the match
        matches.append(best_row)  # Append the result to the matches list

# Convert the matches list into a DataFrame for easy handling
df_matches = pd.DataFrame(matches).set_index('index')

# Merge df_a with df_matches, adding columns from df_b (with "_b" suffix)
df_result = df_a.join(df_matches, rsuffix='_b')

# Display the final matched DataFrame
print(df_result)

# The output shows the original df_a along with the matched records from df_b, including the match score.

#     ssn       name   amount        ssn_b     name_b   id  last4       score
# 0  2334    ana dow  1500.00  098-77-2334    ana dew  105   2334   85.714286
# 1  2334     an dee   235.36  234-09-2334   anna dee  101   2334   85.714286
# 2  1235  anna smit   965.25  321-76-1235  anna smit  102   1235  100.000000
# 3  4567    any rod    50.10  890-87-4567   anna rod  103   4567  100.000000


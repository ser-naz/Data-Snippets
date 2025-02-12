import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame with Country Population Data in millions
data = {
    "Country": ["Germany", "France", "Italy", "Spain", "Poland"],
    "Population": [83000000, 67000000, 60000000, 47000000, 38000000]}
df = pd.DataFrame(data)

# Convert Population to Millions by dividing by 1 million
df["Population"] = df["Population"] / 1_000_000

# Define a function to display both values and percentages
def func(pct, allval):
    absolute = round(pct / 100.*allval, 2)  # Calculate the actual value from percentage
    return f"{absolute}M\n({pct:.1f}%)"  # Return both value and percentage

# Set the figure size to make the pie chart round
plt.figure(figsize=(14, 9))
# Plot a pie chart with both values and percentages inside the slices
plt.pie(df["Population"], labels=df["Country"], autopct=lambda pct: func(pct, sum(df["Population"])),
        startangle=140, colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"])

# Add a title
plt.title("Population Distribution by Country (in Millions)", fontsize=17, fontweight='bold')

plt.show()

# **********************************************************************************************************************

# Same output with fig, ax = plt.subplots()
# Create figure and axes
fig, ax = plt.subplots(figsize=(14, 9))

# Plot a pie chart with both values and percentages inside the slices
ax.pie(df["Population"], labels=df["Country"], autopct=lambda pct: func(pct, sum(df["Population"])),
       startangle=140, colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"])

# Add a title
ax.set_title("Population Distribution by Country (in Millions)", fontsize=17, fontweight='bold')

# plt.show()
# **********************************************************************************************************************
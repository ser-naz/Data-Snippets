import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame with Population data for Female and Male in different countries
data = {
    "Country": ["Germany", "France", "Italy", "Spain", "Poland", "Netherlands", "Ukraine"],
    "Female Population": [42600000, 34200000, 30600000, 23900000, 19300000, 8600000, 23000000],
    "Male Population": [40500000, 33100000, 29600000, 22800000, 19000000, 8530000, 22000000]}
df = pd.DataFrame(data)

# Set up the figure size for the plot
plt.figure(figsize=(10, 6))

# Set the x-axis positions for the bars (representing the countries). Return range
x = range(len(df))  # Create a sequence of numbers representing each country's bar position on the x-axis

# Define the width of the bars to fit both Male and Female bars side by side
width = 0.4

# Plot Female bars will be slightly shifted to the left (by width/2)
female_bars = plt.bar([i - width/2 for i in x], df["Female Population"], width=width, label="Female", color="lightblue")

# Plot Male bars will be shifted to the right (by width/2)
male_bars = plt.bar([i + width/2 for i in x], df["Male Population"], width=width, label="Male", color="lightcoral")

# Add axis labels and a title to the chart
plt.xlabel("Country", fontsize=15)
plt.ylabel("Population", fontsize=15)
plt.title("Population by Gender in European Countries", fontsize=18, fontweight='bold')

# Add x-axis tick labels (the country names)
plt.xticks(x, df["Country"], rotation=45, ha="right")

# Add a legend to differentiate between Male and Female bars
plt.legend()

# Annotate for Female bars, display the population number in millions with one decimal point
for bar in female_bars:
    height = bar.get_height()  # Get the height of each Female bar (population value)
    # Annotate inside the bar (vertically centered) with the population in millions (rounded to 1 decimal)
    plt.text(bar.get_x() + bar.get_width() / 2, height / 2, f"{height / 1000000:.1f}M",
             ha='center', va='center', fontsize=10, color="blue", rotation=90)  # Use blue for Female bars

# Annotate for Male bars, display the population number in millions with one decimal point
for bar in male_bars:
    height = bar.get_height()  # Get the height of each Male bar (population value)
    # Annotate inside the bar (vertically centered) with the population in millions (rounded to 1 decimal)
    plt.text(bar.get_x() + bar.get_width() / 2, height / 2, f"{height / 1000000:.1f}M",
             ha='center', va='center', fontsize=10, color="red", rotation=90)  # Use red for Male bars

# Find the maximum population value (Male or Female) to dynamically set the y-axis limit
max_population_female = df["Female Population"].max()  # Get the highest Female population
max_population_male = df["Male Population"].max()  # Get the highest Male population
population = max([max_population_female, max_population_male])  # Find the larger of the two
max_population = population  # Set max_population as the larger value

# Set the y-axis limit dynamically to accommodate the largest population value
plt.ylim(0, max_population * 1.1)  # Set the y-axis range from 0 to 10% higher than the max population value

# Format the y-ticks to display population in millions (e.g., 10M, 20M, etc.)
yticks_values = [i * 10000000 for i in range(0, int(max_population / 10000000) + 1)]  # Calculate the y-ticks in 10 million increments
plt.yticks(yticks_values, [f'{i // 1000000}M' for i in yticks_values])  # Display the y-ticks in millions (e.g., 10M, 20M, etc.)

# Display the plot with tight layout for proper spacing
plt.tight_layout()

plt.show()

# **********************************************************************************************************************

# Same output with fig, ax = plt.subplots()
# Create the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Set the x-axis positions for the bars (representing the countries)
x = range(len(df))  # Create a sequence of numbers representing each country's bar position on the x-axis

# Define the width of the bars to fit both Male and Female bars side by side
width = 0.4

# Plot Female bars
female_bars = ax.bar([i - width/2 for i in x], df["Female Population"], width=width, label="Female", color="lightblue")

# Plot Male bars
male_bars = ax.bar([i + width/2 for i in x], df["Male Population"], width=width, label="Male", color="lightcoral")

# Add axis labels and a title to the chart
ax.set_xlabel("Country", fontsize=15)
ax.set_ylabel("Population", fontsize=15)
ax.set_title("Population by Gender in European Countries", fontsize=18, fontweight='bold')

# Add x-axis tick labels (the country names)
ax.set_xticks(x)
ax.set_xticklabels(df["Country"], rotation=45, ha="right")

# Add a legend to differentiate between Male and Female bars
ax.legend()

# Annotate for Female bars
for bar in female_bars:
    height = bar.get_height()  # Get the height of each Female bar (population value)
    ax.text(bar.get_x() + bar.get_width() / 2, height / 2, f"{height / 1000000:.1f}M",
            ha='center', va='center', fontsize=10, color="blue", rotation=90)

# Annotate for Male bars
for bar in male_bars:
    height = bar.get_height()  # Get the height of each Male bar (population value)
    ax.text(bar.get_x() + bar.get_width() / 2, height / 2, f"{height / 1000000:.1f}M",
            ha='center', va='center', fontsize=10, color="red", rotation=90)

# Find the maximum population value (Male or Female)
max_population_female = df["Female Population"].max()  # Get the highest Female population
max_population_male = df["Male Population"].max()  # Get the highest Male population
population = max([max_population_female, max_population_male])  # Find the larger of the two
max_population = population  # Set max_population as the larger value

# Set the y-axis limit dynamically to accommodate the largest population value
ax.set_ylim(0, max_population * 1.1)  # Set the y-axis range from 0 to 10% higher than the max population value

# Format the y-ticks to display population in millions
yticks_values = [i * 10000000 for i in range(0, int(max_population / 10000000) + 1)]  # Calculate the y-ticks in 10 million increments
ax.set_yticks(yticks_values)
ax.set_yticklabels([f'{i // 1000000}M' for i in yticks_values])  # Display the y-ticks in millions

# Display the plot with tight layout for proper spacing
plt.tight_layout()

# Show the plot
# plt.show()
# **********************************************************************************************************************

import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame  with GDP per capita for several countries across different years.
data = {
    "Country": ["Germany", "France", "Italy", "Spain", "Poland"],
    "2018": [45000, 42000, 38000, 35000, 15000],
    "2019": [46000, 43000, 39000, 36000, 16000],
    "2020": [47000, 44000, 40000, 37000, 17000],
    "2021": [48000, 45000, 41000, 38000, 18000],
    "2022": [49000, 46000, 42000, 39000, 19000]}
df = pd.DataFrame(data)

# Set the 'Country' column as the index
df.set_index("Country", inplace=True)

# Convert GDP values to thousands for readability
df = df / 1000  # Dividing by 1000

# Create the heatmap
# Create a figure with custom size
plt.figure(figsize=(10, 6))

# Using imshow to create the heatmap. The "YlGnBu" colormap ranges from yellow (low) to blue (high).
# aspect='auto' ensures the aspect ratio adjusts automatically for a good fit in the plot.
plt.imshow(df, cmap="YlGnBu", aspect="auto")  # Generate the heatmap

# Add a Colorbar
# It provides a scale for interpreting the heatmap values.
cbar = plt.colorbar()  # Add a colorbar to the plot
cbar.set_label("GDP per Capita (in $ Thousands)", fontsize=12)

# Add labels for the axes
# We use df.columns for the x-axis (years) and df.index for the y-axis (countries).
# The x-ticks are rotated by 45 degrees for readability.
plt.xticks(ticks=range(len(df.columns)), labels=df.columns, fontsize=10, rotation=45)
plt.yticks(ticks=range(len(df.index)), labels=df.index, fontsize=10)  # Set y-ticks with country names

# Add Title
plt.title("Heatmap of GDP Per Capita by Country and Year", fontsize=16, fontweight="bold")
# Label axes for clarity
plt.xlabel("Year", fontsize=12)
plt.ylabel("Country", fontsize=12)

# Add Annotations. Each cell in the heatmap will be annotated with the GDP value (in thousands).
# We use plt.text() to add the text at each (x, y) location with formatting.
for i in range(len(df.index)):  # Loop through rows (countries)
    for j in range(len(df.columns)):  # Loop through columns (years)
        value = df.iloc[i, j]  # Get the value of GDP for the specific country and year
        plt.text(
            j, i,  # x and y positions in the plot
            f"{value:.1f}",  # Display GDP value, rounded to 1 decimal place
            ha="center", va="center",  # Center the text in each cell
            color="black", fontsize=9  # Black color for text and small font size
        )

# Adjust Layout. Use plt.tight_layout() to automatically adjust the layout and avoid overlapping text.
plt.tight_layout()

plt.show()  # Display the heatmap
# **********************************************************************************************************************

# Same output with fig, ax = plt.subplots()
# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create the heatmap
cax = ax.imshow(df, cmap="YlGnBu", aspect="auto")  # Generate the heatmap

# Add a Colorbar
cbar = fig.colorbar(cax, ax=ax)
cbar.set_label("GDP per Capita (in $ Thousands)", fontsize=12)

# Add labels for the axes
ax.set_xticks(range(len(df.columns)))
ax.set_xticklabels(df.columns, fontsize=10, rotation=45)
ax.set_yticks(range(len(df.index)))
ax.set_yticklabels(df.index, fontsize=10)

# Add Title
ax.set_title("Heatmap of GDP Per Capita by Country and Year", fontsize=16, fontweight="bold")

# Label axes for clarity
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Country", fontsize=12)

# Add Annotations
for i in range(len(df.index)):  # Loop through rows (countries)
    for j in range(len(df.columns)):  # Loop through columns (years)
        value = df.iloc[i, j]  # Get the value of GDP for the specific country and year
        ax.text(
            j, i,  # x and y positions in the plot
            f"{value:.1f}",  # Display GDP value, rounded to 1 decimal place
            ha="center", va="center",  # Center the text in each cell
            color="black", fontsize=9  # Black color for text and small font size
        )

# Adjust layout
plt.tight_layout()

plt.show()  # Display the heatmap
# **********************************************************************************************************************
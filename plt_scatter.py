import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create dataframe
data = {
    "Experience (Years)": [1, 3, 5, 7, 10, 12, 15, 18, 20, 25, 30],
    "Salary ($)": [35000, 42000, 48000, 55000, 75000, 85000, 105000, 115000, 120000, 135000, 150000]}
df = pd.DataFrame(data)


# Colors and sizes for the scatter points
colors = np.linspace(0, 1, len(df))
sizes = df["Salary ($)"] / 1000  # Scale sizes based on salary

# Set figure size
plt.figure(figsize=(14, 9))

# Create the scatter plot
scatter = plt.scatter(
    df["Experience (Years)"],
    df["Salary ($)"],
    c=colors,
    s=sizes,
    edgecolor='black')

# Add titles and labels
plt.title("Experience vs. Salary", fontsize=20, fontweight='bold')
plt.xlabel("Experience (Years)", fontsize=15)
plt.ylabel("Salary ($)", fontsize=15)

# Set up limits for y-axis
plt.ylim(20000, 160000)

# Add grid lines
plt.grid(True, linestyle='--', alpha=0.6)

# Add a color bar
cbar = plt.colorbar(scatter)
cbar.set_label('Color Intensity (Proportional to Experience)', fontsize=12)

# Annotate points. y + 2000 moves the label slightly above the data point
for i, (x, y) in enumerate(zip(df["Experience (Years)"], df["Salary ($)"])):
    plt.text(x, y + 2000, f"${y // 1000}k", fontsize=9, color="blue", ha="center")

plt.show()
# **********************************************************************************************************************

# Same output with fig, ax = plt.subplots()
# Create figure and axes
fig, ax = plt.subplots(figsize=(14, 9))

# Create the scatter plot
scatter = ax.scatter(
    df["Experience (Years)"],
    df["Salary ($)"],
    c=colors,
    s=sizes,
    edgecolor='black')

# Add titles and labels
ax.set_title("Experience vs. Salary", fontsize=20, fontweight='bold')
ax.set_xlabel("Experience (Years)", fontsize=15)
ax.set_ylabel("Salary ($)", fontsize=15)

# Set up limits for y-axis
ax.set_ylim(20000, 160000)

# Add grid lines
ax.grid(True, linestyle='--', alpha=0.6)

# Add a color bar
cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label('Color Intensity (Proportional to Experience)', fontsize=12)

# Annotate points. y + 2000 moves the label slightly above the data point
for i, (x, y) in enumerate(zip(df["Experience (Years)"], df["Salary ($)"])):
    ax.text(x, y + 2000, f"${y // 1000}k", fontsize=9, color="blue", ha="center")

# plt.show()
# **********************************************************************************************************************

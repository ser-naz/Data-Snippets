import matplotlib.pyplot as plt
import pandas as pd

# Create dataframe
data = {'Year':['Quarter 1', 'Quarter 2', 'Quarter 3','Quarter 4'], 'Sale':[2500, 6000, 12300, 11250]}
df = pd.DataFrame(data)


# Set up figure size. It must be before plt.plot
plt.figure(figsize=(13, 8))

# Create the plot
plt.plot(df.Year, df.Sale, marker='o')

# Add grid lines
plt.grid(True, linewidth=0.5, linestyle='--', color='gray', alpha=0.7)

# Add titles and labels
plt.title('Sales by Quarter', fontsize=22)
plt.ylabel('Sales', fontsize=15)
plt.xlabel('Quarter', fontsize=15)

# Set up limits for x/y axis. plt.axis([xmin, xmax, ymin, ymax]) can be used instead ylim and xlim.
plt.ylim(0, 14000)
plt.xlim(-0.5, len(df.Year) - 0.5)

# Add text labels for each data point
for i, sale in enumerate(df.Sale):
    plt.text(df.Year[i], sale + 200, f'{sale}', ha='right', fontsize=10, color='black')

# Rotate x-axis tick labels
plt.xticks(rotation=45)

plt.show()

# **********************************************************************************************************************

# Same output with fig, ax = plt.subplots()
# Set up figure and axes
fig, ax = plt.subplots(figsize=(13, 8))

# Create the plot
ax.plot(df.Year, df.Sale, marker='o', linestyle='-', color='b')

# Add grid lines
ax.grid(True, linewidth=0.5, linestyle='--', color='gray', alpha=0.7)

# Add titles and labels
ax.set_title('Sales by Quarter', fontsize=22)
ax.set_ylabel('Sales', fontsize=15)
ax.set_xlabel('Quarter', fontsize=15)

# Set axis limits
ax.set_ylim(0, 14000)

# Add text labels for each data point
for i, sale in enumerate(df.Sale):
    ax.text(df.Year[i], sale + 300, f'{sale}', ha='center', fontsize=12, color='black')

# Rotate x-axis tick labels
ax.set_xticks(df.Year)
plt.xticks(rotation=45)

# plt.show()
# **********************************************************************************************************************

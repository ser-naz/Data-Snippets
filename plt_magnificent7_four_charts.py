import matplotlib.pyplot as plt
import pandas as pd

# Create a dictionary containing data for the 7 companies in the S&P 500
data = {
    "Company": ["Apple", "Microsoft", "Alphabet", "Amazon", "Nvidia", "Tesla", "Meta"],
    "Market Cap (Billion)": [2700, 2100, 1600, 1300, 800, 700, 800],  # Market Cap in Billion USD
    "Revenue (Billion)": [365, 200, 300, 470, 30, 70, 120],  # Revenue in Billion USD
    "Profit (Billion)": [100, 75, 70, 25, 15, 10, 30],  # Profit in Billion USD
    "Stock Price (USD)": [175, 300, 2750, 3400, 1500, 900, 400],  # Stock price in USD
    "YoY Growth (%)": [6, 8, 10, 12, 15, 20, 5]}  # Year-over-Year Growth Percentage

df = pd.DataFrame(data)


# Create a 2x2 grid for subplots (4 charts) with a custom figure size
fig, axs = plt.subplots(2, 2, figsize=(14, 12))


# Pie Chart - Market Cap Distribution
# Create a pie chart on the first subplot (top-left)
axs[0, 0].pie(df["Market Cap (Billion)"],  # Values for the pie slices (market cap)
              labels=df["Company"],  # Labels for each slice (company names)
              autopct=lambda pct: f"{pct:.1f}%",  # Format percentage values to 1 decimal place
              startangle=90)  # Start angle for better visual alignment
axs[0, 0].set_title("Market Cap Distribution")  # Set title for the pie chart


# Bar Chart - Revenue by Company
# Create a bar chart on the second subplot (top-right)
axs[0, 1].bar(df["Company"],  # X-axis values (company names)
              df["Revenue (Billion)"],  # Y-axis values (revenue for each company)
              color="skyblue")  # Color of the bars
axs[0, 1].set_title("Revenue by Company")  # Set title for the bar chart
axs[0, 1].set_ylabel("Revenue (Billions)")  # Set label for the Y-axis


# Scatter Plot - Stock Price vs Profit
# Create a scatter plot on the third subplot (bottom-left)
scatter = axs[1, 0].scatter(df["Stock Price (USD)"],  # X-axis values (stock prices)
                            df["Profit (Billion)"],  # Y-axis values (profits)
                            color="green",  # Color for the scatter points
                            s=100)  # Size of the scatter points
axs[1, 0].set_title("Stock Price vs Profit")  # Set title for the scatter plot
axs[1, 0].set_xlabel("Stock Price (USD)")  # Set label for the X-axis
axs[1, 0].set_ylabel("Profit (Billion USD)")  # Set label for the Y-axis
fig.colorbar(scatter, ax=axs[1, 0], label="Stock Price (USD)")  # Add a color bar to indicate the stock price range


# Heatmap - Correlation Between Market Cap, Revenue, and Profit
# Calculate the correlation matrix between market cap, revenue, and profit
correlation_matrix = df[["Market Cap (Billion)", "Revenue (Billion)", "Profit (Billion)"]].corr()

# Create the heatmap on the fourth subplot (bottom-right)
cax = axs[1, 1].imshow(correlation_matrix,  # Correlation matrix for the heatmap
                       cmap="coolwarm",  # Color map for the heatmap (cool to warm colors)
                       aspect="auto")  # Automatically adjust aspect ratio
axs[1, 1].set_title("Correlation Between Market Cap, Revenue, and Profit")  # Set title for the heatmap
axs[1, 1].set_xlabel("Metric")  # Set label for the X-axis
axs[1, 1].set_ylabel("Metric")  # Set label for the Y-axis

# Set the ticks for the heatmap's axes
axs[1, 1].set_xticks(range(len(correlation_matrix.columns)))  # Position of the X-axis ticks
axs[1, 1].set_xticklabels(correlation_matrix.columns, rotation=45)  # Label the X-axis ticks with column names (rotated for readability)
axs[1, 1].set_yticks(range(len(correlation_matrix.index)))  # Position of the Y-axis ticks
axs[1, 1].set_yticklabels(correlation_matrix.index)  # Label the Y-axis ticks with index names (correlation metrics)
fig.colorbar(cax, ax=axs[1, 1], label="Correlation")  # Add a color bar to show the correlation scale

# Annotate the correlation values in each cell of the heatmap
for i in range(len(correlation_matrix.index)):  # Loop over rows
    for j in range(len(correlation_matrix.columns)):  # Loop over columns
        value = correlation_matrix.iloc[i, j]  # Get the value from the correlation matrix
        axs[1, 1].text(j, i, f"{value:.2f}", ha="center", va="center", color="black", fontsize=12)  # Add text annotation to each cell

# Automatically adjusts subplot parameters to prevent overlap
plt.tight_layout()
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 4, 5, 6],
    'D': [9, 8, 7, 6, 5]
}

df = pd.DataFrame(data)
print(df)
# Calculate the correlation matrix
corr_matrix = df.corr()
print(corr_matrix)
# Plot the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)

# Show the plot
plt.title("Heatmap of Correlation Matrix")
plt.show()

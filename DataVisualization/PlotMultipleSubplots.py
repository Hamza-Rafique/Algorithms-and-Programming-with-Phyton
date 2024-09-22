import matplotlib.pyplot as plt
import numpy as np

# Create sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x / 10)

# Create a figure and multiple subplots (2 rows, 2 columns)
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plotting on each subplot
axes[0, 0].plot(x, y1, color='blue')
axes[0, 0].set_title('Sine Function')

axes[0, 1].plot(x, y2, color='green')
axes[0, 1].set_title('Cosine Function')

axes[1, 0].plot(x, y3, color='red')
axes[1, 0].set_title('Tangent Function')

axes[1, 1].plot(x, y4, color='purple')
axes[1, 1].set_title('Exponential Function')

# Adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()

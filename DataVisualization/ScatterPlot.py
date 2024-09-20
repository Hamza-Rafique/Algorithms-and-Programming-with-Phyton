import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [9, 7, 5, 6, 3, 8, 2, 4, 1]

plt.scatter(x, y, color='blue', label="Data Points")

plt.title("Sample Scatter Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.legend()

plt.show()

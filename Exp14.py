import numpy as np
import matplotlib.pyplot as plt

# Create a figure with subplots (3 rows, 3 columns)
fig, axes = plt.subplots(3, 3, figsize=(15, 15))

# Line Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
axes[0, 0].plot(x, y, label="Sine Wave", color="blue")
axes[0, 0].set_title("Line Plot")
axes[0, 0].legend()

# Scatter Plot
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
axes[0, 1].scatter(x_scatter, y_scatter, color="red", marker="o", alpha=0.7)
axes[0, 1].set_title("Scatter Plot")

# Bar Plot
categories = ["A", "B", "C", "D"]
values = [10, 20, 15, 25]
axes[0, 2].bar(categories, values, color="green")
axes[0, 2].set_title("Bar Plot")

# Histogram
data_hist = np.random.randn(1000)
axes[1, 0].hist(data_hist, bins=30, color="blue", edgecolor="black", alpha=0.7)
axes[1, 0].set_title("Histogram")

# Pie Chart
labels = ["A", "B", "C", "D"]
sizes = [25, 35, 20, 20]
axes[1, 1].pie(sizes, labels=labels, autopct="%1.1f%%", colors=["red", "blue", "green", "yellow"])
axes[1, 1].set_title("Pie Chart")

# Box Plot
data_box = [np.random.randn(100), np.random.randn(100), np.random.randn(100)]
axes[1, 2].boxplot(data_box, labels=["Group 1", "Group 2", "Group 3"])
axes[1, 2].set_title("Box Plot")

# Heatmap
matrix = np.random.rand(10, 10)
img = axes[2, 0].imshow(matrix, cmap="coolwarm", interpolation="nearest")
fig.colorbar(img, ax=axes[2, 0])  # Add color bar
axes[2, 0].set_title("Heatmap")

# Adjust layout
plt.tight_layout()
plt.show()

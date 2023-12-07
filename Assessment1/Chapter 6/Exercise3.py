import matplotlib.pyplot as plt

# Draw a line from (1, 2) to (6, 8)
plt.plot([1, 6], [2, 8], label='Solid Line')

# Draw a dotted line from (1, 3) to (2, 8), then to (6, 1), and finally to (8, 10)
plt.plot([1, 2, 6, 8], [3, 8, 1, 10], linestyle='dotted', label='Dotted Line')

# Set labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line Plots')

# Add legend
plt.legend()

# Display the plot
plt.show()

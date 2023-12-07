import matplotlib.pyplot as plt

# Data
brands = ["Amazon", "Apple", "Google", "Microsoft", "Walmart", "Samsung Group", "ICBC", "Verizon", "Tesla", "TikTok/Douyin"]
values = [299.28, 297.51, 281.38, 191.57, 113.78, 99.66, 69.55, 67.44, 66.21, 65.67]

# Create a bar graph
plt.figure(figsize=(10, 6))
plt.barh(brands, values, color='skyblue')
plt.xlabel('Brand Value (Billion U.S. Dollars)')
plt.title('Most Valuable Brands Worldwide in 2023')
plt.grid(axis='x')

# Display the graph
plt.show()

a = [20, 23, 82, 40, 32, 15, 67, 52]

# Find the indices of even numbers
even_indices = [i for i, num in enumerate(a) if num % 2 == 0]
print("Indices of even numbers:", even_indices)

# Sort the array
sorted_a = sorted(a)
print("Sorted array:", sorted_a)

# Slice elements from index 3 to the end of the array
slice1 = a[3:]
print("Slice from index 3 to end:", slice1)

# Slice elements from index 0 to index 4
slice2 = a[:5]
print("Slice from index 0 to 4:", slice2)

# Print [32, 15, 67] using negative slicing
slice3 = a[-5:-2]
print("Slice using negative slicing:", slice3)

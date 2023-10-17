# Create an integer list with 10 values
integer_list = [5, 12, 8, 3, 15, 7, 10, 2, 9, 6]

# Output the list using a for loop
print("List elements:")
for num in integer_list:
    print(num, end=' ')
print()

# Output the highest and lowest value
highest_value = max(integer_list)
lowest_value = min(integer_list)
print(f"Highest value: {highest_value}")
print(f"Lowest value: {lowest_value}")

# Sort the elements in ascending order
ascending_sorted_list = sorted(integer_list)
print("Sorted in ascending order:", ascending_sorted_list)

# Sort the elements in descending order
descending_sorted_list = sorted(integer_list, reverse=True)
print("Sorted in descending order:", descending_sorted_list)

# Append two elements
integer_list.append(11)
integer_list.append(4)

# Print the list after appending
print("List after appending:")
for num in integer_list:
    print(num, end=' ')

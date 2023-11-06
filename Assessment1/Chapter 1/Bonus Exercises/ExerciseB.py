# Define the list
locations = ['Philippines', 'Davao', 'Manila', 'Cebu', 'Bohol', 'Cavite']

# Print the list and find its length
print("Original List:", locations)
print("Length of the list:", len(locations))

# Use sorted() to print the list in alphabetical order without modifying the actual list
sorted_list_alpha = sorted(locations)
print("Sorted in alphabetical order:", sorted_list_alpha)

# Print the original list to show it is still in its original order
print("Original List (unchanged):", locations)

# Use sorted() to print the list in reverse alphabetical order without changing the original list
sorted_list_rev_alpha = sorted(locations, reverse=True)
print("Sorted in reverse alphabetical order:", sorted_list_rev_alpha)

# Print the original list to show it is still in its original order
print("Original List (unchanged):", locations)

# Use reverse() to change the order of the list
locations.reverse()
print("List after using reverse():", locations)

# Use sort() to change the list to alphabetical order
locations.sort()
print("List after using sort() (alphabetical order):", locations)

# Use sort() to change the list to reverse alphabetical order
locations.sort(reverse=True)
print("List after using sort() (reverse alphabetical order):", locations)

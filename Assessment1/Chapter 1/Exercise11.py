# Create the tuple
year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

# Access the value at index -3
value_at_minus_three = year[-3]
print(f"Value at index -3: {value_at_minus_three}")

# Reverse the tuple and print both the original and reversed tuples
reversed_year = tuple(reversed(year))
print(f"Original tuple: {year}")
print(f"Reversed tuple: {reversed_year}")

# Count the number of times 2009 is in the tuple
count_2009 = year.count(2009)
print(f"Number of times 2009 appears: {count_2009}")

# Get the index value of 2018
index_2018 = year.index(2018)
print(f"Index of 2018: {index_2018}")

# Find the length of the tuple
length_of_tuple = len(year)
print(f"Length of the tuple: {length_of_tuple}")

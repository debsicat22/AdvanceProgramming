def calculate_product(values):
    product = 1
    for value in values:
        product *= value
    return product

# Define a list
my_list = [2, 3, 5, 7, 11]

# Call the function and pass the list as an argument
result = calculate_product(my_list)

# Print the result
print(f"The product of the values in the list is: {result}")

# Prompt the user to input their name
name = input("Hello, user!\nWhat is your name?\n").title()

# Prompt the user to input their age
age = int(input("What is your age?\n"))

# Print a greeting with the formatted name
print(f"It is good to meet you, {name}")

# Find the length of the name
name_length = len(name)

# Calculate the age after one year
age_next_year = age + 1

# Print the length of the name and the age after one year
print(f"The length of your name is:\n{name_length}")
print(f"You will be {age_next_year} in a year.")

# Read numbers from file and create a list
with open('numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

# Output the values
print("List of integers:")
for number in numbers:
    print(number)

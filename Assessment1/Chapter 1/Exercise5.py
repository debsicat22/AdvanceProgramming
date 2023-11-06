# Initialize a counter for the number of times the loop is executed
count = 0

# Start a while loop
while True:
    user_input = input("Do you want to continue? (Y/N)").upper()
    if user_input != 'Y':
        break
    count += 1

# Output the number of times the loop was executed
print(f"The loop was executed {count} times.")

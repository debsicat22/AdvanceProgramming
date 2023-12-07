#Formula of the number given by the user
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Get the input from the user
user_input = input("Enter a positive number: ")

number = int(user_input)

#Apply the formula
result = factorial(number)
print("The factorial of", number, "is:", result)

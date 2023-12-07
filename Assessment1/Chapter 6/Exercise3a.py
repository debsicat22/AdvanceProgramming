import operator

def calculator_menu():
    # Display the calculator menu options
    print("Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Check greater number")

def get_user_choice():
    while True:
        # Get user choice and handle invalid input
        choice = input("Enter your choice (1-6) or 'Q' to quit: ").upper()
        if choice == 'Q':
            return None
        elif choice.isdigit() and 1 <= int(choice) <= 6:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 6 or 'Q' to quit.")

def get_user_input():
    try:
        # Get user input for two numbers and handle invalid input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None

def perform_operation(choice, num1, num2):
    # Define a dictionary to map user choice to corresponding operator functions
    operations = {
        1: operator.add,
        2: operator.sub,
        3: operator.mul,
        4: operator.truediv,
        5: operator.mod,
        6: max
    }
    # Perform the chosen operation and display the result
    operation = operations[choice]
    result = operation(num1, num2)
    print(f"Result: {result}")

def main():
    while True:
        # Display the menu and get user choice
        calculator_menu()
        choice = get_user_choice()
        if choice is None:
            print("Exiting the calculator. Goodbye!")
            break

        # Get user input for numbers and perform the chosen operation
        user_input = get_user_input()
        if user_input is not None:
            perform_operation(choice, *user_input)

if __name__ == "__main__":
    main()

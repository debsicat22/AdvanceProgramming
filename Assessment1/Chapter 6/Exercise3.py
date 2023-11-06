import operator

def add(a, b):
    return operator.add(a, b)

def subtract(a, b):
    return operator.sub(a, b)

def multiply(a, b):
    return operator.mul(a, b)

def divide(a, b):
    return operator.truediv(a, b)

def modulus(a, b):
    return operator.mod(a, b)

def check_greater(a, b):
    return operator.gt(a, b)

def get_user_input():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None, None

def display_menu():
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Check greater number")
    print("Q. Quit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6, Q to quit): ")

        if choice == '1':
            num1, num2 = get_user_input()
            if num1 is not None and num2 is not None:
                result = add(num1, num2)
                print("Result:", result)

        elif choice == '2':
            num1, num2 = get_user_input()
            if num1 is not None and num2 is not None:
                result = subtract(num1, num2)
                print("Result:", result)

        elif choice == '3':
            num1, num2 = get_user_input()
            if num1 is not None and num2 is not None:
                result = multiply(num1, num2)
                print("Result:", result)

        elif choice == '4':
            num1, num2 = get_user_input()
            if num1 is not None and num2 is not None:
                if num2 != 0:
                    result = divide(num1, num2)
                    print("Result:", result)
                else:
                    print("Error: Division by zero")

        elif choice == '5':
            num1, num2 = get_user_input()
            if num1 is not None and num2 is not None:
                if num2 != 0:
                    result = modulus(num1, num2)
                    print("Result:", result)
                else:
                    print("Error: Modulus by zero")

        elif choice == '6':
            num1, num2 = get_user_input()
            if num1 is not None and num2 is not None:
                result = check_greater(num1, num2)
                print(f"{num1} is greater than {num2}: {result}")

        elif choice.upper() == 'Q':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

def display_menu():
    print("\nWelcome to Burger Shack!")
    print("1. Beef Burger")
    print("2. Chicken Burger")
    print("3. Vegetarian Burger")

def choose_burger():
    choice = input("Please select a burger type (1-3): ")
    if choice == '1':
        return "Beef Burger"
    elif choice == '2':
        return "Chicken Burger"
    elif choice == '3':
        return "Vegetarian Burger"
    else:
        print("Invalid choice. Please try again.")
        return choose_burger()

def add_toppings():
    toppings = []
    while True:
        print("\nChoose a topping (or press Enter to finish): ")
        print("1. Cheese")
        print("2. Peanut Butter")
        print("3. Avocado")
        choice = input()
        if choice == '1':
            toppings.append("Cheese")
        elif choice == '2':
            toppings.append("Peanut Butter")
        elif choice == '3':
            toppings.append("Avocado")
        elif choice == '':
            break
        else:
            print("Invalid choice. Please try again.")
    return toppings

def add_condiments():
    condiments = []
    while True:
        print("\nChoose a condiment (or press Enter to finish): ")
        print("1. Ketchup")
        print("2. Mayonnaise")
        print("3. BBQ Sauce")
        choice = input()
        if choice == '1':
            condiments.append("Ketchup")
        elif choice == '2':
            condiments.append("Mayonnaise")
        elif choice == '3':
            condiments.append("BBQ Sauce")
        elif choice == '':
            break
        else:
            print("Invalid choice. Please try again.")
    return condiments

def add_sides():
    sides = []
    while True:
        print("\nChoose a side (or press Enter to finish): ")
        print("1. Fries")
        print("2. Drink")
        choice = input()
        if choice == '1':
            sides.append("Fries")
        elif choice == '2':
            sides.append("Drink")
        elif choice == '':
            break
        else:
            print("Invalid choice. Please try again.")
    return sides

def calculate_total(order):
    prices = {
        "Beef Burger": 10.0,
        "Chicken Burger": 8.0,
        "Vegetarian Burger": 7.0,
        "Cheese": 1.0,
        "Peanut Butter": 1.5,
        "Avocado": 2.0,
        "Ketchup": 0.5,
        "Mayonnaise": 0.5,
        "BBQ Sauce": 0.5,
        "Fries": 2.0,
        "Drink": 1.5
    }

    total = sum(prices[item] for item in order)
    return total

def main():
    order = []
    display_menu()
    burger_choice = choose_burger()
    order.append(burger_choice)

    toppings = add_toppings()
    order.extend(toppings)

    condiments = add_condiments()
    order.extend(condiments)

    sides = add_sides()
    order.extend(sides)

    total = calculate_total(order)

    print("\nOrder Summary:")
    for item in order:
        print(f"- {item}")
    print(f"\nTotal: ${total}")

    payment = float(input("Enter the payment amount: $"))
    change = payment - total

    print(f"Change: ${change:.2f}")
    print("Thank you for ordering from Burger Shack!")

if __name__ == "__main__":
    main()

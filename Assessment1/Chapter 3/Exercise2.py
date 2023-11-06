import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

def order_coffee():
    selected_coffee = coffee_var.get()
    options = []

    if sugar_var.get():
        options.append("Sugar")

    if milk_var.get():
        options.append("Milk")

    if chocolate_var.get():
        options.append("Chocolate")

    message = f"You ordered a {selected_coffee} coffee with {', '.join(options)}."
    messagebox.showinfo("Order Confirmation", message)

root = tk.Tk()
root.title("Coffee Vending Machine")
root.geometry("500x500")

# Coffee Options
coffee_var = tk.StringVar(value="Espresso")
coffee_label = ttk.Label(root, text="Select Coffee Type:")
coffee_label.pack()

coffee_options = ttk.Combobox(root, textvariable=coffee_var, values=["Espresso", "Latte", "Cappuccino"])
coffee_options.pack()

# Additional Options
sugar_var = tk.BooleanVar(value=False)
milk_var = tk.BooleanVar(value=False)
chocolate_var = tk.BooleanVar(value=False)

sugar_checkbox = ttk.Checkbutton(root, text="Sugar", variable=sugar_var)
sugar_checkbox.pack()

milk_checkbox = ttk.Checkbutton(root, text="Milk", variable=milk_var)
milk_checkbox.pack()

chocolate_checkbox = ttk.Checkbutton(root, text="Chocolate", variable=chocolate_var)
chocolate_checkbox.pack()

# Load and display resized images
espresso_image = Image.open("espresso.jpg")
espresso_image = espresso_image.resize((100, 100))
espresso_photo = ImageTk.PhotoImage(espresso_image)
espresso_label = ttk.Label(root, image=espresso_photo)
espresso_label.pack()

latte_image = Image.open("latte.jpg")
latte_image = latte_image.resize((100, 100))
latte_photo = ImageTk.PhotoImage(latte_image)
latte_label = ttk.Label(root, image=latte_photo)
latte_label.pack()

cappuccino_image = Image.open("cappuccino.jpg")
cappuccino_image = cappuccino_image.resize((100, 100))
cappuccino_photo = ImageTk.PhotoImage(cappuccino_image)
cappuccino_label = ttk.Label(root, image=cappuccino_photo)
cappuccino_label.pack()

# Order Button
order_button = ttk.Button(root, text="Order Coffee", command=order_coffee)
order_button.pack()

root.mainloop()

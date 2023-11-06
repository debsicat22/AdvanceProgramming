import tkinter as tk
from tkinter import ttk
from math import pi

class Shape:
    def __init__(self):
        self.sides = []

    def inputSides(self):
        pass

class Circle(Shape):
    def inputSides(self):
        radius = float(entry_radius.get())
        self.sides.append(radius)

    def area(self):
        return pi * (self.sides[0] ** 2)

class Rectangle(Shape):
    def inputSides(self):
        length = float(entry_length.get())
        width = float(entry_width.get())
        self.sides.extend([length, width])

    def area(self):
        return self.sides[0] * self.sides[1]

class Triangle(Shape):
    def inputSides(self):
        base = float(entry_base.get())
        height = float(entry_height.get())
        self.sides.extend([base, height])

    def area(self):
        return 0.5 * self.sides[0] * self.sides[1]

def calculate_area():
    shape = shape_combobox.get()
    if shape == "Circle":
        circle = Circle()
        circle.inputSides()
        result_label.config(text=f"Area: {circle.area()} square units")
    elif shape == "Rectangle":
        rectangle = Rectangle()
        rectangle.inputSides()
        result_label.config(text=f"Area: {rectangle.area()} square units")
    elif shape == "Triangle":
        triangle = Triangle()
        triangle.inputSides()
        result_label.config(text=f"Area: {triangle.area()} square units")

root = tk.Tk()
root.title("Shape Area Calculator")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, padx=10, pady=10)

shape_label = ttk.Label(frame, text="Select Shape:")
shape_label.grid(row=0, column=0, padx=5, pady=5)

shapes = ["Circle", "Rectangle", "Triangle"]
shape_combobox = ttk.Combobox(frame, values=shapes, state="readonly")
shape_combobox.grid(row=0, column=1, padx=5, pady=5)
shape_combobox.current(0)

calculate_button = ttk.Button(frame, text="Calculate Area", command=calculate_area)
calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Circle
radius_label = ttk.Label(frame, text="Radius:")
radius_label.grid(row=2, column=0, padx=5, pady=5)
entry_radius = ttk.Entry(frame)
entry_radius.grid(row=2, column=1, padx=5, pady=5)

# Rectangle
length_label = ttk.Label(frame, text="Length:")
length_label.grid(row=3, column=0, padx=5, pady=5)
entry_length = ttk.Entry(frame)
entry_length.grid(row=3, column=1, padx=5, pady=5)

width_label = ttk.Label(frame, text="Width:")
width_label.grid(row=4, column=0, padx=5, pady=5)
entry_width = ttk.Entry(frame)
entry_width.grid(row=4, column=1, padx=5, pady=5)

# Triangle
base_label = ttk.Label(frame, text="Base:")
base_label.grid(row=5, column=0, padx=5, pady=5)
entry_base = ttk.Entry(frame)
entry_base.grid(row=5, column=1, padx=5, pady=5)

height_label = ttk.Label(frame, text="Height:")
height_label.grid(row=6, column=0, padx=5, pady=5)
entry_height = ttk.Entry(frame)
entry_height.grid(row=6, column=1, padx=5, pady=5)

result_label = ttk.Label(frame, text="Area:")
result_label.grid(row=7, column=0, columnspan=2, pady=(10, 0))

root.mainloop()

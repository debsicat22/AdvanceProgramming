import tkinter as tk
from tkinter import ttk
import math

def calculate_circle_area():
    radius = float(circle_radius_entry.get())
    area = math.pi * (radius ** 2)
    circle_result_label.config(text=f"Area of Circle: {area:.2f}")

def calculate_square_area():
    side = float(square_side_entry.get())
    area = side ** 2
    square_result_label.config(text=f"Area of Square: {area:.2f}")

def calculate_rectangle_area():
    length = float(rectangle_length_entry.get())
    width = float(rectangle_width_entry.get())
    area = length * width
    rectangle_result_label.config(text=f"Area of Rectangle: {area:.2f}")

# Create main window
root = tk.Tk()
root.title("Area Calculator")
root.geometry("400x300")

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(root)

# Circle tab
circle_tab = ttk.Frame(notebook)
notebook.add(circle_tab, text="Circle")

circle_radius_label = ttk.Label(circle_tab, text="Enter radius:")
circle_radius_label.grid(row=0, column=0, padx=5, pady=5)

circle_radius_entry = ttk.Entry(circle_tab)
circle_radius_entry.grid(row=0, column=1, padx=5, pady=5)

circle_calculate_button = ttk.Button(circle_tab, text="Calculate", command=calculate_circle_area)
circle_calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

circle_result_label = ttk.Label(circle_tab, text="Area of Circle: ")
circle_result_label.grid(row=2, column=0, columnspan=2)

# Square tab
square_tab = ttk.Frame(notebook)
notebook.add(square_tab, text="Square")

square_side_label = ttk.Label(square_tab, text="Enter side length:")
square_side_label.grid(row=0, column=0, padx=5, pady=5)

square_side_entry = ttk.Entry(square_tab)
square_side_entry.grid(row=0, column=1, padx=5, pady=5)

square_calculate_button = ttk.Button(square_tab, text="Calculate", command=calculate_square_area)
square_calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

square_result_label = ttk.Label(square_tab, text="Area of Square: ")
square_result_label.grid(row=2, column=0, columnspan=2)

# Rectangle tab
rectangle_tab = ttk.Frame(notebook)
notebook.add(rectangle_tab, text="Rectangle")

rectangle_length_label = ttk.Label(rectangle_tab, text="Enter length:")
rectangle_length_label.grid(row=0, column=0, padx=5, pady=5)

rectangle_length_entry = ttk.Entry(rectangle_tab)
rectangle_length_entry.grid(row=0, column=1, padx=5, pady=5)

rectangle_width_label = ttk.Label(rectangle_tab, text="Enter width:")
rectangle_width_label.grid(row=1, column=0, padx=5, pady=5)

rectangle_width_entry = ttk.Entry(rectangle_tab)
rectangle_width_entry.grid(row=1, column=1, padx=5, pady=5)

rectangle_calculate_button = ttk.Button(rectangle_tab, text="Calculate", command=calculate_rectangle_area)
rectangle_calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

rectangle_result_label = ttk.Label(rectangle_tab, text="Area of Rectangle: ")
rectangle_result_label.grid(row=3, column=0, columnspan=2)

# Pack the notebook
notebook.pack(padx=10, pady=10, fill='both', expand=True)

root.mainloop()

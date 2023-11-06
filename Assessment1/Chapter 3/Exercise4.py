import tkinter as tk
from tkinter import ttk


def draw_shape():
    canvas.delete("all")
    shape = shape_var.get()

    if shape == "Oval":
        x1 = int(x1_entry.get())
        y1 = int(y1_entry.get())
        x2 = int(x2_entry.get())
        y2 = int(y2_entry.get())
        canvas.create_oval(x1, y1, x2, y2, fill="blue")

    elif shape == "Rectangle":
        x1 = int(x1_entry.get())
        y1 = int(y1_entry.get())
        x2 = int(x2_entry.get())
        y2 = int(y2_entry.get())
        canvas.create_rectangle(x1, y1, x2, y2, fill="red")

    elif shape == "Square":
        x1 = int(x1_entry.get())
        y1 = int(y1_entry.get())
        side = int(side_entry.get())
        x2 = x1 + side
        y2 = y1 + side
        canvas.create_rectangle(x1, y1, x2, y2, fill="green")

    elif shape == "Triangle":
        x1 = int(x1_entry.get())
        y1 = int(y1_entry.get())
        x2 = int(x2_entry.get())
        y2 = int(y2_entry.get())
        x3 = int(x3_entry.get())
        y3 = int(y3_entry.get())
        canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="purple")


# Create main window
root = tk.Tk()
root.title("Shape Drawer")

# Create frame for input
input_frame = ttk.Frame(root)
input_frame.pack(padx=10, pady=10)

# Create labels and entry fields for coordinates
shape_var = tk.StringVar()
shape_var.set("Oval")
shape_label = ttk.Label(input_frame, text="Select Shape:")
shape_label.grid(row=0, column=0, padx=5, pady=5)

shape_dropdown = ttk.Combobox(input_frame, textvariable=shape_var, values=["Oval", "Rectangle", "Square", "Triangle"])
shape_dropdown.grid(row=0, column=1, padx=5, pady=5)

x1_label = ttk.Label(input_frame, text="x1:")
x1_label.grid(row=1, column=0, padx=5, pady=5)
x1_entry = ttk.Entry(input_frame)
x1_entry.grid(row=1, column=1, padx=5, pady=5)

y1_label = ttk.Label(input_frame, text="y1:")
y1_label.grid(row=2, column=0, padx=5, pady=5)
y1_entry = ttk.Entry(input_frame)
y1_entry.grid(row=2, column=1, padx=5, pady=5)

x2_label = ttk.Label(input_frame, text="x2:")
x2_label.grid(row=3, column=0, padx=5, pady=5)
x2_entry = ttk.Entry(input_frame)
x2_entry.grid(row=3, column=1, padx=5, pady=5)

y2_label = ttk.Label(input_frame, text="y2:")
y2_label.grid(row=4, column=0, padx=5, pady=5)
y2_entry = ttk.Entry(input_frame)
y2_entry.grid(row=4, column=1, padx=5, pady=5)

x3_label = ttk.Label(input_frame, text="x3:")
x3_label.grid(row=5, column=0, padx=5, pady=5)
x3_entry = ttk.Entry(input_frame)
x3_entry.grid(row=5, column=1, padx=5, pady=5)

y3_label = ttk.Label(input_frame, text="y3:")
y3_label.grid(row=6, column=0, padx=5, pady=5)
y3_entry = ttk.Entry(input_frame)
y3_entry.grid(row=6, column=1, padx=5, pady=5)

side_label = ttk.Label(input_frame, text="Side Length:")
side_label.grid(row=7, column=0, padx=5, pady=5)
side_entry = ttk.Entry(input_frame)
side_entry.grid(row=7, column=1, padx=5, pady=5)

# Create button to draw shape
draw_button = ttk.Button(input_frame, text="Draw Shape", command=draw_shape)
draw_button.grid(row=8, column=0, columnspan=2, pady=10)

# Create canvas for drawing
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(padx=10, pady=10)

root.mainloop()

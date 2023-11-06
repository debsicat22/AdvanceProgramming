import tkinter as tk
from tkinter import ttk

def update_greeting():
    name = name_entry.get()
    color = color_var.get()
    greeting = f"Hello, {name}!"
    display_label.config(text=greeting, foreground=color)

# Create main window
root = tk.Tk()
root.title("Greeting App")
root.geometry("600x400")

# Create InputFrame with blue background
input_frame = ttk.Frame(root, padding=10, style="Input.TFrame")
input_frame.grid(row=0, column=0, padx=10, pady=10)

# Create DisplayFrame with green background
display_frame = ttk.Frame(root, padding=10, style="Display.TFrame", width=200)
display_frame.grid(row=0, column=1, padx=10, pady=10)

# Create a custom style for the frames
style = ttk.Style()

# Style for InputFrame
style.configure("Input.TFrame", background="#87CEFA")

# Style for DisplayFrame
style.configure("Display.TFrame", background="#98FB98")

# Create widgets for InputFrame
title_label = ttk.Label(input_frame, text="Welcome!", font=("Helvetica", 16, "bold"), foreground="blue")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

name_label = ttk.Label(input_frame, text="Name:")
name_label.grid(row=1, column=0, sticky="w")

name_entry = ttk.Entry(input_frame)
name_entry.grid(row=1, column=1, pady=5)

color_label = ttk.Label(input_frame, text="Select Color:")
color_label.grid(row=2, column=0, sticky="w")

color_var = tk.StringVar(value="black")
color_dropdown = ttk.Combobox(input_frame, textvariable=color_var, values=["black", "red", "blue", "green"])
color_dropdown.grid(row=2, column=1, pady=5)

update_button = ttk.Button(input_frame, text="Update Greeting", command=update_greeting)
update_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create a label for DisplayFrame
display_label = ttk.Label(display_frame, font=("Helvetica", 14), anchor="center")
display_label.pack(expand=True, fill="both")

root.mainloop()

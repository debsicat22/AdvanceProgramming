import tkinter as tk
from tkinter import ttk

class Animal:
    def __init__(self):
        self.type = ""
        self.name = ""
        self.color = ""
        self.age = 0
        self.weight = 0.0
        self.noise = ""

    def say_hello(self):
        return f"{self.name} says hello!"

    def make_noise(self):
        return f"{self.name} makes a {self.noise} noise."

    def animal_details(self):
        return f"Type: {self.type}, Name: {self.name}, Color: {self.color}, Age: {self.age}, Weight: {self.weight}, Noise: {self.noise}"

def get_animal_details():
    animal = Animal()
    animal.type = entry_type.get()
    animal.name = entry_name.get()
    animal.color = entry_color.get()
    animal.age = int(entry_age.get())
    animal.weight = float(entry_weight.get())
    animal.noise = entry_noise.get()

    details_label.config(text=animal.animal_details())

root = tk.Tk()
root.title("Animal Details")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, padx=10, pady=10)

type_label = ttk.Label(frame, text="Type:")
type_label.grid(row=0, column=0, padx=5, pady=5)
entry_type = ttk.Entry(frame)
entry_type.grid(row=0, column=1, padx=5, pady=5)

name_label = ttk.Label(frame, text="Name:")
name_label.grid(row=1, column=0, padx=5, pady=5)
entry_name = ttk.Entry(frame)
entry_name.grid(row=1, column=1, padx=5, pady=5)

color_label = ttk.Label(frame, text="Color:")
color_label.grid(row=2, column=0, padx=5, pady=5)
entry_color = ttk.Entry(frame)
entry_color.grid(row=2, column=1, padx=5, pady=5)

age_label = ttk.Label(frame, text="Age:")
age_label.grid(row=3, column=0, padx=5, pady=5)
entry_age = ttk.Entry(frame)
entry_age.grid(row=3, column=1, padx=5, pady=5)

weight_label = ttk.Label(frame, text="Weight:")
weight_label.grid(row=4, column=0, padx=5, pady=5)
entry_weight = ttk.Entry(frame)
entry_weight.grid(row=4, column=1, padx=5, pady=5)

noise_label = ttk.Label(frame, text="Noise:")
noise_label.grid(row=5, column=0, padx=5, pady=5)
entry_noise = ttk.Entry(frame)
entry_noise.grid(row=5, column=1, padx=5, pady=5)

details_button = ttk.Button(frame, text="Get Details", command=get_animal_details)
details_button.grid(row=6, column=0, columnspan=2, pady=10)

details_label = ttk.Label(frame, text="Details:")
details_label.grid(row=7, column=0, columnspan=2)

root.mainloop()

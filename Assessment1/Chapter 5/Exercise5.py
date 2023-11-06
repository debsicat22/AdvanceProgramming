import tkinter as tk
from tkinter import ttk

class Animal:
    def __init__(self, Type, Name, Colour, Age, Weight, Noise):
        self.Type = Type
        self.Name = Name
        self.Colour = Colour
        self.Age = Age
        self.Weight = Weight
        self.Noise = Noise

    def sayHello(self):
        print(f"{self.Name} says hello!")

    def makeNoise(self):
        print(f"{self.Name} makes a {self.Noise} noise!")

    def animalDetails(self):
        details = f"Type: {self.Type}\nName: {self.Name}\nColour: {self.Colour}\nAge: {self.Age}\nWeight: {self.Weight}\nNoise: {self.Noise}"
        return details

def create_animal():
    Type = entry_type.get()
    Name = entry_name.get()
    Colour = entry_colour.get()
    Age = int(entry_age.get())
    Weight = float(entry_weight.get())
    Noise = entry_noise.get()

    new_animal = Animal(Type, Name, Colour, Age, Weight, Noise)
    new_animal.sayHello()
    new_animal.makeNoise()

    result_label.config(text=new_animal.animalDetails())

root = tk.Tk()
root.title("Animal Interaction")
root.geometry("350x500")

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

colour_label = ttk.Label(frame, text="Colour:")
colour_label.grid(row=2, column=0, padx=5, pady=5)
entry_colour = ttk.Entry(frame)
entry_colour.grid(row=2, column=1, padx=5, pady=5)

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

create_button = ttk.Button(frame, text="Create Animal", command=create_animal)
create_button.grid(row=6, column=0, columnspan=2, pady=10)

result_label = ttk.Label(frame, text="")
result_label.grid(row=7, column=0, columnspan=2, pady=(0, 10))

root.mainloop()

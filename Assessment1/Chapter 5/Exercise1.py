import tkinter as tk
from tkinter import messagebox

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def woof(self):
        return f"{self.name} says: Woof!"

def create_dog():
    name = name_entry.get()
    breed = breed_entry.get()
    age = age_entry.get()

    try:
        age = int(age)
        dog = Dog(name, breed, age)
        dogs.append(dog)
        display_dogs()
        messagebox.showinfo("Success", f"{dog.name} has been created!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid age (integer).")

def display_dogs():
    display_text.delete(1.0, tk.END)
    for dog in dogs:
        display_text.insert(tk.END, f"Name: {dog.name}\nBreed: {dog.breed}\nAge: {dog.age}\n\n")

def oldest_dog():
    oldest = max(dogs, key=lambda x: x.age)
    messagebox.showinfo("Oldest Dog", oldest.woof())

dogs = []

root = tk.Tk()
root.title("Dog Information")

name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

breed_label = tk.Label(root, text="Breed:")
breed_label.grid(row=1, column=0, padx=10, pady=5)
breed_entry = tk.Entry(root)
breed_entry.grid(row=1, column=1, padx=10, pady=5)

age_label = tk.Label(root, text="Age:")
age_label.grid(row=2, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=5)

create_button = tk.Button(root, text="Create Dog", command=create_dog)
create_button.grid(row=3, column=0, columnspan=2, pady=10)

display_text = tk.Text(root, width=40, height=10)
display_text.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

oldest_button = tk.Button(root, text="Oldest Dog", command=oldest_dog)
oldest_button.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()

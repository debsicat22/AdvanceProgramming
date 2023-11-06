import tkinter as tk

def save_to_file():
    name = name_entry.get()
    age = age_entry.get()
    hometown = hometown_entry.get()

    with open("bio.txt", "w") as file:
        file.write(f"Name: {name}\nAge: {age}\nHometown: {hometown}")

def read_from_file():
    with open("bio.txt", "r") as file:
        content = file.read()
        output_label.config(text=content)

# Create main window
root = tk.Tk()
root.title("Bio Information")
root.geometry("500x400")

# Create labels and entry fields
name_label = tk.Label(root, text="Name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()

age_entry = tk.Entry(root)
age_entry.pack()

hometown_label = tk.Label(root, text="Hometown:")
hometown_label.pack()

hometown_entry = tk.Entry(root)
hometown_entry.pack()

# Create buttons
save_button = tk.Button(root, text="Save to File", command=save_to_file)
save_button.pack()

read_button = tk.Button(root, text="Read from File", command=read_from_file)
read_button.pack()

# Create label to display output
output_label = tk.Label(root, text="", wraplength=300)
output_label.pack()

# Start the tkinter event loop
root.mainloop()

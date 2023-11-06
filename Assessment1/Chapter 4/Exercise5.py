import tkinter as tk
from tkinter import messagebox

def validate_password():
    password = password_entry.get()
    attempts = 5

    while attempts > 0:
        if (
            any(char.islower() for char in password) and
            any(char.isdigit() for char in password) and
            any(char.isupper() for char in password) and
            any(char in "$#@." for char in password) and
            6 <= len(password) <= 12
        ):
            messagebox.showinfo("Password Valid", "Password is valid!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                messagebox.showwarning("Invalid Password", f"Incorrect password! {attempts} attempts remaining.")
                password_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Alert", "Authorities have been alerted! Too many failed attempts.")
                root.destroy()

# Create main window
root = tk.Tk()
root.title("Password Validator")
root.geometry("300x300")

# Create password entry and label
password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=10)

# Create validate button
validate_button = tk.Button(root, text="Validate Password", command=validate_password)
validate_button.pack(pady=20)

# Start the tkinter event loop
root.mainloop()

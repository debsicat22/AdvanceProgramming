import tkinter as tk
from tkinter import ttk


def on_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "user" and password == "pass":
        result = "Login successful!"
    else:
        result = "Invalid username or password."

    tk.messagebox.showinfo("Result", result, parent=root)


root = tk.Tk()
root.title("Login Page")
root.geometry("400x300")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

username_label = ttk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

username_entry = ttk.Entry(root, width=20)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = ttk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

password_entry = ttk.Entry(root, width=20, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

login_button = ttk.Button(root, text="Login", command=on_login)
login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

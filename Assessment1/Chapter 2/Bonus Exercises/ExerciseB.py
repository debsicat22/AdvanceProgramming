from datetime import datetime

def calculate_age():
    try:
        dob = datetime.strptime(entry.get(), "%d/%m/%Y")
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        result_label.config(text=f"Your age is {age} years")
    except ValueError:
        result_label.config(text="Please enter a valid date in the format dd/mm/yyyy")

import tkinter as tk

root = tk.Tk()
root.title("Age Calculator")

# Date of Birth Entry
dob_label = tk.Label(root, text="Enter your date of birth (dd/mm/yyyy):")
dob_label.pack(pady=(10, 0))
entry = tk.Entry(root)
entry.pack(pady=(0, 10))

# Calculate Age Button
calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack()

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=(10, 0))

# Run the main event loop
root.mainloop()

import tkinter as tk
from tkinter import ttk, PhotoImage

# Create main window
root = tk.Tk()
root.title("Student Management System")
root.geometry("550x900")

# Create a custom style for the frame
style = ttk.Style()
style.configure("TFrame", background="#f4f4f6")

imagelogo = PhotoImage(file="logoimage.png")
imagelogo_label = ttk.Label(root, image=imagelogo)
imagelogo_label.pack(pady=(20, 0))

# Create header labels
header_label1 = ttk.Label(root, text="Student Management System", font=("Helvetica", 20, "bold"))
header_label1.pack(pady=(20, 10))

header_label2 = ttk.Label(root, text="New Student Registration", font=("Helvetica", 16, "bold"))
header_label2.pack(pady=(0, 20))
# Create a Frame
frame = ttk.Frame(root, padding="50", style="TFrame")
frame.pack()

# Create Entry widgets for data input
name_entry = ttk.Entry(frame)
name_entry.grid(row=0, column=1, padx=10, pady=10)

mobile_entry = ttk.Entry(frame)
mobile_entry.grid(row=1, column=1, padx=10, pady=10)

email_entry = ttk.Entry(frame)
email_entry.grid(row=2, column=1, padx=10, pady=10)

home_address_entry = ttk.Entry(frame)
home_address_entry.grid(row=3, column=1, padx=10, pady=10)

gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(frame, textvariable=gender_var)
gender_combobox.grid(row=4, column=1, padx=10, pady=10)
gender_combobox['values'] = ('Male', 'Female', 'Other')

course_var = tk.StringVar()
course_combobox = ttk.Combobox(frame, textvariable=course_var)
course_combobox.grid(row=5, column=1, padx=10, pady=10)
course_combobox['values'] = ('BSc CC', 'BSc CY', 'BSc PSY', 'BA & BM')

language_var = tk.StringVar()
language_combobox = ttk.Combobox(frame, textvariable=language_var)
language_combobox.grid(row=6, column=1, padx=10, pady=10)
language_combobox['values'] = ('English', 'Tagalog', 'Hindi / Urdu')

# Create Label widgets for data input
name_label = ttk.Label(frame, text="Student Name")
name_label.grid(row=0, column=0, padx=10, pady=10)

mobile_label = ttk.Label(frame, text="Mobile Number")
mobile_label.grid(row=1, column=0, padx=10, pady=10)

email_label = ttk.Label(frame, text="Email Id")
email_label.grid(row=2, column=0, padx=10, pady=10)

home_address_label = ttk.Label(frame, text="Home Address")
home_address_label.grid(row=3, column=0, padx=10, pady=10)

gender_label = ttk.Label(frame, text="Gender")
gender_label.grid(row=4, column=0, padx=10, pady=10)

course_label = ttk.Label(frame, text="Course Enrolled")
course_label.grid(row=5, column=0, padx=10, pady=10)

language_label = ttk.Label(frame, text="Language Known")
language_label.grid(row=6, column=0, padx=10, pady=10)

# New Label for English communication skills
english_rating_label = ttk.Label(frame, text="Rate your English communication skills")
english_rating_label.grid(row=7, column=0, padx=10, pady=10)

# Slider for English communication skills
english_rating = ttk.Scale(frame, from_=0, to=10, orient=tk.HORIZONTAL, length=150)
english_rating.grid(row=7, column=1, padx=10, pady=10)


# Create a Button
style = ttk.Style()
style.configure("TButton", background="#22263d")

add_button = ttk.Button(frame, text="Submit", style="TButton")
add_button.grid(row=8, column=0, padx=20, pady=50)
clear_button = ttk.Button(frame, text="Clear", style="TButton")
clear_button.grid(row=8, column=1, padx=20, pady=50)

root.mainloop()
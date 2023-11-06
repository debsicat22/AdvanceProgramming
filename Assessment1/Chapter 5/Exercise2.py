import tkinter as tk

class Students:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calcGrade(self):
        return (self.mark1 + self.mark2 + self.mark3) / 3

    def display(self):
        average = self.calcGrade()
        return f"Name: {self.name}\nAverage Grade: {average:.2f}"

def create_student():
    name = name_entry.get()
    mark1 = int(mark1_entry.get())
    mark2 = int(mark2_entry.get())
    mark3 = int(mark3_entry.get())

    student = Students(name, mark1, mark2, mark3)
    result_label.config(text=student.display())

root = tk.Tk()
root.title("Student Grade Calculator")
root.geometry("300x400")

name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

mark1_label = tk.Label(root, text="Mark 1:")
mark1_label.grid(row=1, column=0, padx=10, pady=5)
mark1_entry = tk.Entry(root)
mark1_entry.grid(row=1, column=1, padx=10, pady=5)

mark2_label = tk.Label(root, text="Mark 2:")
mark2_label.grid(row=2, column=0, padx=10, pady=5)
mark2_entry = tk.Entry(root)
mark2_entry.grid(row=2, column=1, padx=10, pady=5)

mark3_label = tk.Label(root, text="Mark 3:")
mark3_label.grid(row=3, column=0, padx=10, pady=5)
mark3_entry = tk.Entry(root)
mark3_entry.grid(row=3, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate Grade", command=create_student)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()

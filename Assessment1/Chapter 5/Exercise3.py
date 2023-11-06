import tkinter as tk

class Employee:
    def __init__(self):
        self.name = ""
        self.age = ""
        self.id = ""
        self.salary = ""

    def setData(self, name, age, emp_id, salary):
        self.name = name
        self.age = age
        self.id = emp_id
        self.salary = salary

    def getData(self):
        return f"{self.name}\t{self.age}\t{self.salary}\t{self.id}"

employees = []

def add_employee():
    name = name_entry.get()
    age = age_entry.get()
    emp_id = id_entry.get()
    salary = salary_entry.get()

    emp = Employee()
    emp.setData(name, age, emp_id, salary)
    employees.append(emp)

def display_employees():
    for emp in employees:
        result_text.insert(tk.END, emp.getData() + "\n")

root = tk.Tk()
root.title("Employee Management")

tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Age").grid(row=1, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="ID").grid(row=2, column=0, padx=10, pady=5)
id_entry = tk.Entry(root)
id_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Salary").grid(row=3, column=0, padx=10, pady=5)
salary_entry = tk.Entry(root)
salary_entry.grid(row=3, column=1, padx=10, pady=5)

add_button = tk.Button(root, text="Add Employee", command=add_employee)
add_button.grid(row=4, column=0, columnspan=2, pady=10)

display_button = tk.Button(root, text="Display Employees", command=display_employees)
display_button.grid(row=5, column=0, columnspan=2, pady=10)

result_text = tk.Text(root, height=10, width=40)
result_text.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()

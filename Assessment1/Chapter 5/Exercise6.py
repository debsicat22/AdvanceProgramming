import tkinter as tk
from tkinter import ttk

class ArithmeticOperations:
    def __init__(self):
        self.result = 0

    def calculate(self, operation, num1, num2):
        if operation == "Addition":
            self.result = num1 + num2
        elif operation == "Subtraction":
            self.result = num1 - num2
        elif operation == "Multiplication":
            self.result = num1 * num2
        elif operation == "Division":
            self.result = num1 / num2

def perform_calculation():
    operation = operation_combobox.get()
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())

    calculator = ArithmeticOperations()
    calculator.calculate(operation, num1, num2)
    result_label.config(text=f"Result: {calculator.result}")

root = tk.Tk()
root.title("Arithmetic Operations")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, padx=10, pady=10)

operation_label = ttk.Label(frame, text="Operation:")
operation_label.grid(row=0, column=0, padx=5, pady=5)
operation_options = ["Addition", "Subtraction", "Multiplication", "Division"]
operation_combobox = ttk.Combobox(frame, values=operation_options)
operation_combobox.grid(row=0, column=1, padx=5, pady=5)

num1_label = ttk.Label(frame, text="Number 1:")
num1_label.grid(row=1, column=0, padx=5, pady=5)
entry_num1 = ttk.Entry(frame)
entry_num1.grid(row=1, column=1, padx=5, pady=5)

num2_label = ttk.Label(frame, text="Number 2:")
num2_label.grid(row=2, column=0, padx=5, pady=5)
entry_num2 = ttk.Entry(frame)
entry_num2.grid(row=2, column=1, padx=5, pady=5)

calculate_button = ttk.Button(frame, text="Calculate", command=perform_calculation)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = ttk.Label(frame, text="Result:")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()

from tkinter import *

def click(event):
    button = event.widget
    action = button.cget("text")
    num1 = int(e1.get())
    num2 = int(e2.get())
    if action == "ADD":
        controller.add(num1, num2)
    elif action == "SUBTRACT":
        controller.subtract(num1, num2)
    elif action == "MULTIPLY":
        controller.multiply(num1, num2)
    elif action == "DIVIDE":
        controller.divide(num1, num2)
    elif action == "MODULO":
        controller.modulo(num1, num2)
    label.config(text="Result: " + str(controller.get_result()))

class CalculatorController:
    def __init__(self):
        self.result = 0

    def add(self, num1, num2):
        self.result = num1 + num2

    def subtract(self, num1, num2):
        self.result = num1 - num2

    def multiply(self, num1, num2):
        self.result = num1 * num2

    def divide(self, num1, num2):
        self.result = num1 / num2

    def modulo(self, num1, num2):
        self.result = num1 % num2

    def get_result(self):
        return self.result

controller = CalculatorController()

# Creating the GUI window
root = Tk()
root.title("Simple Calculator")

# Creating widgets
label = Label(root, text="Result: 0")
label.grid(row=0, column=0, columnspan=3)

e1 = Entry(root)
e1.grid(row=1, column=0)

e2 = Entry(root)
e2.grid(row=1, column=1)

add_button = Button(root, text="ADD")
add_button.bind("<Button-1>", click)
add_button.grid(row=2, column=0)

subtract_button = Button(root, text="SUBTRACT")
subtract_button.bind("<Button-1>", click)
subtract_button.grid(row=2, column=1)

multiply_button = Button(root, text="MULTIPLY")
multiply_button.bind("<Button-1>", click)
multiply_button.grid(row=2, column=2)

divide_button = Button(root, text="DIVIDE")
divide_button.bind("<Button-1>", click)
divide_button.grid(row=3, column=0)

modulo_button = Button(root, text="MODULO")
modulo_button.bind("<Button-1>", click)
modulo_button.grid(row=3, column=1)

root.mainloop()
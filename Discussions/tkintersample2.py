from tkinter import *

root = Tk()
root.title("GUI Example 4")

bA = Label(root, text="A", width=12, bg="red", relief=GROOVE , bd=5)
bB = Label(root, text="B", width=12, bg="yellow")
bC = Label(root, text="C", width=12, bg="blue")
bD = Label(root, text="D", width=12, bg="white")

bA.pack(side="top", fill=X, expand=1)
bB.pack(side="bottom")
bC.pack(side="left", fill=X, expand=1)
bD.pack(side="right")

root.mainloop()
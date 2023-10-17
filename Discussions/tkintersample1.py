from tkinter import *

root = Tk()
root.title("GUI Example 3")
root.geometry("350x250")

def copytext():
    print(texts.get())


b1 = Button(root, text="Copy Text", command=copytext)
b1.pack(side="bottom")
l1 = Label(root, text="Copy Text")
l1.pack(side="bottom")
e1 = Entry(root, textvariable=texts)
e1.pack(side="bottom")


root.mainloop()

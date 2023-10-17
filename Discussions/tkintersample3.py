from tkinter import *

root = Tk()
root.title("GUI Example 5")

label = Label(root, text="Enter your Password:")
label.pack(fill=Y)
b1 = Button(root, text="Search")
b1.pack(fill=X)
cB = Button(root, text="RememberMe", variable=v, value=True)
Entry(root, width=30)
rBm = Button(root, text="Male", variable=v, value=1)
rBm.pack(fill=X)
rBf = Button(root, text="Female", variable=v, value=2)
rBf.pack(fill=X)
OptionMenu(root, text="Select Country", value= "USA", "UK", "India", "Others")
Scrollbar(root, orient=VERTICAL, command=mytext.yview)


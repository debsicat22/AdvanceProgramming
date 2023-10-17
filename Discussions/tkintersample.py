from tkinter import *
def change_text():
    label.config(text="Changed Text")

root = Tk()
root.title("GUI Example")

root.geometry("350x250")

label = Label(root, text="Change Text")
label.pack(side="bottom", pady=10)

button = Button(root, text="Change Text", command=change_text)
button.pack(side="bottom", pady=10)


root.mainloop()

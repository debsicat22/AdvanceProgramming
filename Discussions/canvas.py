import tkinter as tk
root = tk.Tk()
root.geometry("1920x1080")
canvas = tk.Canvas(root, width=1920, height=1080)
line = canvas.create_line(50,70,100,70,fill='red',width=2)
dotted_line = canvas.create_line(100,100,100,350, fill='green', width=2, dash=(5,5))
rectangle = canvas.create_rectangle(600,100,300,200, fill='blue', width=2)
oval = canvas.create_oval(500,500,700,200, fill='yellow', width=2, outline='red')
text = canvas.create_text(500,50, fill='black', text='Eyy Yow! Who got you smiling like that!')
rectangle2 = canvas.create_rectangle(70,80,100,110, fill='yellow', width=2)
oval2 = canvas.create_oval(170,180,300,310, fill='yellow', width=2, outline='white')
text2 = canvas.create_text(40,30, fill='black',font='arial', text='Hi')
canvas.pack()
root.mainloop()
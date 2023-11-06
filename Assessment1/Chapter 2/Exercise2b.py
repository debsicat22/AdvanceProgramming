import tkinter as tk

# Create main window
root = tk.Tk()
root.geometry("300x200")

# Create left frame
left_frame = tk.Frame(root, borderwidth=5)
left_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

# Create right frame
right_frame = tk.Frame(root, borderwidth=5)
right_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# Create labels A, B, C, and D with border and background color
label_A = tk.Label(left_frame, text="A", border=30, bg="#22263d", fg="white")
label_B = tk.Label(left_frame, text="B", border=30)
label_C = tk.Label(right_frame, text="C", border=30)
label_D = tk.Label(right_frame, text="D", border=30, bg="#22263d", fg="white")


# Pack labels A, B, C, and D inside their respective frames
label_A.pack(side=tk.TOP, expand=True, fill=tk.X)
label_B.pack(side=tk.BOTTOM, expand=True, fill=tk.X)
label_C.pack(side=tk.TOP, expand=True, fill=tk.X)
label_D.pack(side=tk.BOTTOM, expand=True, fill=tk.X)

# Start the tkinter event loop
root.mainloop()



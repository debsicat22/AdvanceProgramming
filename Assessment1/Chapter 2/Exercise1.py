import tkinter as tk
def main():
    root = tk.Tk()
    root.title("Welcome")

    # Change the label font style
    custom_font = ("Arial", 16, "bold")
    label = tk.Label(root, text="tkinter application", font=custom_font)
    label.pack(pady=20)

    # Set the default window size
    root.geometry("600x600")

    # Disable resizing the window
    root.resizable(0, 0)

    # Add background color to the Window
    root.configure(bg="light blue")

    root.mainloop()

if __name__ == "__main__":
    main()

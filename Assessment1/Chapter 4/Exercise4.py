import tkinter as tk

def count_occurrences():
    char = entry.get()
    with open('sentences.txt', 'r') as file:
        content = file.read()
    count = content.count(char)
    result_label.config(text=f"The character '{char}' occurs {count} times.")

# Create main window
root = tk.Tk()
root.title("Character Occurrence Counter")
root.geometry("300x200")

# Create label and entry for character input
char_label = tk.Label(root, text="Enter a character:")
char_label.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a button to trigger the counting
count_button = tk.Button(root, text="Count Occurrences", command=count_occurrences)
count_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the tkinter event loop
root.mainloop()

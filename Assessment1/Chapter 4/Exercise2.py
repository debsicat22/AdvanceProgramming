import tkinter as tk

def count_occurrences():
    search_string = entry.get().strip()
    if search_string:
        with open("sentences.txt", "r") as file:
            content = file.read()
            occurrences = content.lower().count(search_string.lower())
            result_label.config(text=f"The string appears {occurrences} times.")
    else:
        result_label.config(text="Please enter a search string.")

# Create main window
root = tk.Tk()
root.title("String Occurrence Counter")
root.geometry("300x200")

# Create labels and entry field
entry_label = tk.Label(root, text="Enter search string:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

# Create button
count_button = tk.Button(root, text="Count Occurrences", command=count_occurrences)
count_button.pack()

# Create label to display result
result_label = tk.Label(root, text="", wraplength=300)
result_label.pack()

# Start the tkinter event loop
root.mainloop()

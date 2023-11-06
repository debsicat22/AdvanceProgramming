import tkinter as tk

def convert():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{celsius}°C = {fahrenheit}°F")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

root = tk.Tk()
root.title("Temperature Converter")

# Celsius Entry
celsius_label = tk.Label(root, text="Enter Temperature in Celsius:")
celsius_label.pack(pady=(10, 0))
entry = tk.Entry(root)
entry.pack(pady=(0, 10))

# Convert Button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack()

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=(10, 0))

# Run the main event loop
root.mainloop()

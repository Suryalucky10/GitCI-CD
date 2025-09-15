import tkinter as tk
#111hello
# Function to update expression in the entry field
def press(key):
    entry_field.insert(tk.END, key)

# Function to evaluate the expression
def equal_press():
    try:
        result = str(eval(entry_field.get()))
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, result)
    except:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "Error")

# Function to clear the entry field
def clear():
    entry_field.delete(0, tk.END)

# Creating main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry field for input
entry_field = tk.Entry(root, font=("Arial", 18), justify="right")
entry_field.pack(fill=tk.BOTH, ipadx=8, ipady=8, pady=10, padx=10)

# Buttons layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', 'C', '+')
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        if btn_text == "C":
            btn = tk.Button(frame, text=btn_text, font=("Arial", 16), height=2, width=5, 
                            command=clear)
        else:
            btn = tk.Button(frame, text=btn_text, font=("Arial", 16), height=2, width=5,
                            command=lambda b=btn_text: press(b))
        btn.pack(side="left", expand=True, fill="both")

# Equals button
equal_button = tk.Button(root, text="=", font=("Arial", 16), height=2, command=equal_press)
equal_button.pack(expand=True, fill="both", padx=10, pady=5)

root.mainloop()

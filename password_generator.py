import random
import string
import tkinter as tk
from tkinter import ttk

selected_option = None

# define function to generate password
def generate_password(selected_option):
    try:
        length = int(entry.get())
        if selected_option:
            if 1 <= length <= 100:
                if selected_option == 'just numbers':
                    characters = string.digits
                    password = ''.join(random.choice(characters) for _ in range(length))
                    result_label.config(text="Generated Password: " + password)
                elif selected_option == 'just letters':
                    characters = string.ascii_letters
                    password = ''.join(random.choice(characters) for _ in range(length))
                    result_label.config(text="Generated Password: " + password)
                else:
                    characters = string.ascii_letters + string.digits + string.punctuation
                    password = ''.join(random.choice(characters) for _ in range(length))
                    result_label.config(text="Generated Password: " + password)
            else:
                result_label.config(text="Password length must be between 1 and 100")
        else:
            result_label.config(text="Please select a complexity")
    except ValueError:
        result_label.config(text="Oops, please enter a valid number")

# define function to close window
def close_window():
    root.destroy()

options = ['just numbers', 'just letters', 'everything']

# define function to handle selection
def on_select(event):
    selected_option = combo.get()

root = tk.Tk()
root.title("Macie's Password Generator")

root.geometry("800x200")

label = tk.Label(root, text="Select Password complexity:")
label.pack()

combo = ttk.Combobox(root, values=options)
combo.pack()
combo.bind("<<ComboboxSelected>>", on_select)

label = tk.Label(root, text="Enter desired password length (between 1 and 100): ")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Generate password", command=lambda: generate_password(combo.get()))
button.pack()

result_label = tk.Label(root, text="Your password is:")
result_label.pack()

close_button = tk.Button(root, text="Close window", command=close_window)
close_button.pack()

root.mainloop()
import random
import string
import tkinter as tk

# define function to generate password
def generate_password():
    try:
        length = int(entry.get())
        if 1 <= length <= 100:
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            result_label.config(text="Generated Password: " + password)
        else:
            result_label.config(text="Password length must be between 1 and 100")
    except ValueError:
        result_label.config(text="Oops, please enter a valid number")

# define function to close window
def close_window():
    root.destroy()

root = tk.Tk()
root.title("Macie's Password Generator")

root.geometry("800x200")

label = tk.Label(root, text="Enter desired password length (between 1 and 100): ")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Generate password", command=generate_password)
button.pack()

result_label = tk.Label(root, text="Your password is:")
result_label.pack()

close_button = tk.Button(root, text="Close window", command=close_window)
close_button.pack()

root.mainloop()
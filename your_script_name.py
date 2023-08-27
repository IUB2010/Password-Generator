import tkinter as tk
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def btn_click():
    global password
    button2.config(text=password)

def clear_button():
    button2.config(text="")

password = generate_password()
window = tk.Tk()
window.geometry("1500x700")
window.title("Password Generator")

button2 = tk.Label(text="", font=("cascadia code", 50, "bold"))
button2.grid(row=3, column=5)

button_clear = tk.Button(text="Clear", font=("cascadia code", 30, "bold"), command=clear_button)
button_clear.grid(row=3, column=9)

button1 = tk.Button(text="Generate password", font=("cascadia code", 30, "bold"), command=btn_click)
button1.grid(row=2, column=5)

window.mainloop()

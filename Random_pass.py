import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    password_length = int(length_entry.get())
    if password_length <= 0:
        messagebox.showerror("Error", "Password length should be greater than 0")
        return
    
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(password_length))
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()
    pyperclip.copy(password)

def generate_strong_password():
    password_length = int(length_entry.get())
    if password_length <= 0:
        messagebox.showerror("Error", "Password length should be greater than 0")
        return
    
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(password_length))
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def generate_medium_password():
    password_length = int(length_entry.get())
    if password_length <= 0:
        messagebox.showerror("Error", "Password length should be greater than 0")
        return
    
    password_characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(password_characters) for i in range(password_length))
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def generate_weak_password():
    password_length = int(length_entry.get())
    if password_length <= 0:
        messagebox.showerror("Error", "Password length should be greater than 0")
        return
    
    password_characters = string.ascii_lowercase + string.digits
    password = ''.join(random.choice(password_characters) for i in range(password_length))
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Random Password Generator")

strong_button = tk.Button(root, text="Generate Strong Password",bg="yellow", command=generate_strong_password)
strong_button.grid(row=0, column=0, columnspan=2, pady=5)

medium_button = tk.Button(root, text="Generate Medium Password",bg="pink", command=generate_medium_password)
medium_button.grid(row=1, column=0, columnspan=2, pady=5)

weak_button = tk.Button(root, text="Generate Weak Password",bg="grey", command=generate_weak_password)
weak_button.grid(row=2, column=0, columnspan=2, pady=5)

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

length_entry = tk.Entry(root)
length_entry.grid(row=3, column=1, padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Password",bg="red", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

password_label = tk.Label(root, text="Generated Password:")
password_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)

password_entry = tk.Entry(root)
password_entry.grid(row=5, column=1, padx=10, pady=5)

copy_button = tk.Button(root, text="Copy Password",bg="grey", command=copy_password)
copy_button.grid(row=6, column=0, columnspan=2, pady=10)


root.mainloop()

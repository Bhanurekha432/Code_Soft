import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        
        self.title_label = tk.Label(root, text="Password Generator", font=("Arial", 18))
        self.title_label.pack(pady=10)
        
        self.length_label = tk.Label(root, text="Enter password length:", font=("Arial", 12))
        self.length_label.pack()
        
        self.length_entry = tk.Entry(root, width=10)
        self.length_entry.pack(pady=5)
        
        self.include_upper = tk.BooleanVar()
        self.include_lower = tk.BooleanVar()
        self.include_digits = tk.BooleanVar()
        self.include_symbols = tk.BooleanVar()

        tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.include_upper).pack()
        tk.Checkbutton(root, text="Include Lowercase Letters", variable=self.include_lower).pack()
        tk.Checkbutton(root, text="Include Digits", variable=self.include_digits).pack()
        tk.Checkbutton(root, text="Include Symbols", variable=self.include_symbols).pack()
        
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="Your password will appear here", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError
            
            characters = ""
            if self.include_upper.get():
                characters += string.ascii_uppercase
            if self.include_lower.get():
                characters += string.ascii_lowercase
            if self.include_digits.get():
                characters += string.digits
            if self.include_symbols.get():
                characters += string.punctuation
            
            if not characters:
                messagebox.showwarning("Warning", "Please select at least one character type.")
                return
            
            password = "".join(random.choice(characters) for _ in range(length))
            self.result_label.config(text=f"Generated Password: {password}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for length.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

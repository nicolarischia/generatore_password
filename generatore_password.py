import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generatore di Password")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Variabili per i checkbox
        self.include_upper = tk.BooleanVar(value=True)
        self.include_lower = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)

        self.length = tk.IntVar(value=12)

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Lunghezza password:").pack(pady=5)

        length_slider = ttk.Scale(
            self.root, from_=8, to=32, orient="horizontal", variable=self.length
        )
        length_slider.pack(fill="x", padx=20)

        # Checkboxes
        ttk.Checkbutton(
            self.root, text="Lettere maiuscole (A-Z)", variable=self.include_upper
        ).pack(anchor="w", padx=20, pady=2)
        ttk.Checkbutton(
            self.root, text="Lettere minuscole (a-z)", variable=self.include_lower
        ).pack(anchor="w", padx=20, pady=2)
        ttk.Checkbutton(
            self.root, text="Numeri (0-9)", variable=self.include_digits
        ).pack(anchor="w", padx=20, pady=2)
        ttk.Checkbutton(
            self.root, text="Simboli (!@#$...)", variable=self.include_symbols
        ).pack(anchor="w", padx=20, pady=2)

        ttk.Button(self.root, text="Genera Password", command=self.generate_password).pack(pady=15)

        self.password_entry = ttk.Entry(self.root, font=("Helvetica", 14), justify="center")
        self.password_entry.pack(fill="x", padx=20, pady=5)

        ttk.Button(self.root, text="Copia negli appunti", command=self.copy_to_clipboard).pack()

    def generate_password(self):
        length = int(self.length.get())
        chars = ""
        if self.include_upper.get():
            chars += string.ascii_uppercase
        if self.include_lower.get():
            chars += string.ascii_lowercase
        if self.include_digits.get():
            chars += string.digits
        if self.include_symbols.get():
            chars += "!@#$%^&*()-_=+[]{};:,.<>?/"

        if not chars:
            messagebox.showerror("Errore", "Seleziona almeno un tipo di carattere!")
            return

        password = "".join(random.choice(chars) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copiato", "Password copiata negli appunti!")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

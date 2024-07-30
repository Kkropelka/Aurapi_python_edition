import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Zaawansowany Kalkulator")
        self.root.geometry("400x600")
        
        self.create_widgets()

    def create_widgets(self):
        # Entry widget for displaying the expression
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.result_entry = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 24), borderwidth=2, relief="solid")
        self.result_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('√', 5, 0), ('^', 5, 1), ('log', 5, 2), ('π', 5, 3),
            ('(', 6, 0), (')', 6, 1), ('exp', 6, 2), ('C', 6, 3)
        ]
        
        for (text, row, col) in buttons:
            self.create_button(text, row + 1, col)
        
        # Settings button in the top-right corner
        self.settings_button = tk.Button(self.root, text="Ustawienia", font=("Arial", 10), command=self.open_settings)
        self.settings_button.grid(row=0, column=3, padx=5, pady=5, sticky="ne")

        # Add grid row/column configuration to expand buttons
        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.root.grid_columnconfigure(j, weight=1)

    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, font=("Arial", 18), command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def on_button_click(self, char):
        if char == 'C':
            self.result_var.set("0")
        elif char == '=':
            self.calculate_result()
        else:
            self.add_to_expression(char)
    
    def add_to_expression(self, char):
        current_text = self.result_var.get()
        if current_text == "0":
            self.result_var.set(char)
        else:
            self.result_var.set(current_text + char)
    
    def calculate_result(self):
        try:
            expression = self.result_var.get()
            expression = expression.replace('√', 'math.sqrt')
            expression = expression.replace('^', '**')
            expression = expression.replace('log', 'math.log10')
            expression = expression.replace('exp', 'math.exp')
            expression = expression.replace('π', str(math.pi))
            result = eval(expression)
            self.result_var.set(result)
        except Exception:
            messagebox.showerror("Błąd", "Błąd w obliczeniach")
            self.result_var.set("0")
    
    def open_settings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Ustawienia")
        settings_window.geometry("300x150")

        info_text = "Wersja: 2.0.0\nAutor: krpl5_"
        info_label = tk.Label(settings_window, text=info_text, font=("Arial", 14), padx=20, pady=20)
        info_label.pack(expand=True)

        close_button = tk.Button(settings_window, text="Zamknij", command=settings_window.destroy)
        close_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

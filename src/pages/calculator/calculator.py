import tkinter as tk
from math import sin, cos, tan, sqrt, log, pi, e

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gelişmiş Hesap Makinesi")
        self.geometry("400x500")
        self.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        # Ekran
        self.display = tk.Entry(self, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify="right")
        self.display.grid(row=0, column=0, columnspan=5, pady=10, padx=10, sticky="nsew")
        self.display.bind("<Key>", lambda e: "break")  # Klavyeden giriş engelle

        # Butonlar
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("C", 1, 4),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("(", 2, 4),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), (")", 3, 4),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3), ("^", 4, 4),
        ]

        for (text, row, col) in buttons:
            tk.Button(self, text=text, font=("Arial", 14), command=lambda t=text: self.on_button_click(t))\
                .grid(row=row, column=col, pady=5, padx=5, sticky="nsew")

        # Satır ve sütun genişliği ayarı
        for i in range(7):
            self.grid_rowconfigure(i, weight=1)
        for j in range(5):
            self.grid_columnconfigure(j, weight=1)

    def on_button_click(self, button_text):
        if button_text == "C":
            self.display.delete(0, tk.END)
        elif button_text == "=":
            try:
                expression = self.display.get().replace("^", "**")
                result = eval(expression)  # Kullanıcı girişine dikkat edin
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as ex:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Hata")
        else:
            self.display.insert(tk.END, button_text)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()

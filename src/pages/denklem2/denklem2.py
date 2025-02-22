import tkinter as tk
from tkinter import messagebox
import cmath

class SolverWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Denklem Çözücü")
        self.geometry("400x400")

        # Başlık
        tk.Label(self, text="Denklem Çözücü", font=("Arial", 16)).pack(pady=10)

        # İkinci Dereceden Denklemler
        tk.Label(self, text="İkinci Dereceden Denklem: ax^2 + bx + c = 0", font=("Arial", 12)).pack(pady=5)
        self.quadratic_inputs = self.create_input_fields("a", "b", "c")
        tk.Button(self, text="Çöz", command=self.solve_quadratic).pack(pady=10)

        # Üçüncü Dereceden Denklemler
        tk.Label(self, text="Üçüncü Dereceden Denklem: ax^3 + bx^2 + cx + d = 0", font=("Arial", 12)).pack(pady=5)
        self.cubic_inputs = self.create_input_fields("a", "b", "c", "d")
        tk.Button(self, text="Çöz", command=self.solve_cubic).pack(pady=10)

    def create_input_fields(self, *coefficients):
        frame = tk.Frame(self)
        frame.pack(pady=5)
        entries = {}
        for coef in coefficients:
            tk.Label(frame, text=f"{coef}:").pack(side=tk.LEFT, padx=5)
            entry = tk.Entry(frame, width=5)
            entry.pack(side=tk.LEFT, padx=5)
            entries[coef] = entry
        return entries

    def solve_quadratic(self):
        try:
            a = float(self.quadratic_inputs["a"].get())
            b = float(self.quadratic_inputs["b"].get())
            c = float(self.quadratic_inputs["c"].get())

            if a == 0:
                messagebox.showerror("Hata", "a sıfır olamaz!")
                return

            discriminant = cmath.sqrt(b**2 - 4*a*c)
            root1 = (-b + discriminant) / (2*a)
            root2 = (-b - discriminant) / (2*a)

            messagebox.showinfo("Sonuç", f"Kökler: {root1}, {root2}")
        except ValueError:
            messagebox.showerror("Hata", "Lütfen tüm katsayıları doğru formatta giriniz!")

    def solve_cubic(self):
        try:
            a = float(self.cubic_inputs["a"].get())
            b = float(self.cubic_inputs["b"].get())
            c = float(self.cubic_inputs["c"].get())
            d = float(self.cubic_inputs["d"].get())

            if a == 0:
                messagebox.showerror("Hata", "a sıfır olamaz!")
                return

            # Üçüncü dereceden denklemin çözümü
            f = ((3*a*c) - (b**2)) / (3*(a**2))
            g = ((2*(b**3)) - (9*a*b*c) + (27*(a**2)*d)) / (27*(a**3))
            h = (g**2) / 4 + (f**3) / 27

            if h > 0:
                r = -(g / 2) + cmath.sqrt(h)
                s = r**(1/3)
                t = -(g / 2) - cmath.sqrt(h)
                u = t**(1/3)
                root1 = s + u - (b / (3*a))
                messagebox.showinfo("Sonuç", f"Tek gerçek kök: {root1}")
            else:
                # Üç gerçek kök
                i = cmath.sqrt(((g**2) / 4) - h)
                j = i**(1/3)
                k = cmath.acos(-(g / (2 * i)))
                l = -j
                m = cmath.cos(k / 3)
                n = cmath.sqrt(3) * cmath.sin(k / 3)
                p = -(b / (3*a))

                root1 = 2*j*cmath.cos(k/3) - (b/(3*a))
                root2 = l * (m + n) + p
                root3 = l * (m - n) + p

                messagebox.showinfo("Sonuç", f"Kökler: {root1}, {root2}, {root3}")
        except ValueError:
            messagebox.showerror("Hata", "Lütfen tüm katsayıları doğru formatta giriniz!")

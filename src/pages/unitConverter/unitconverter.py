import tkinter as tk
from tkinter import ttk

class UnitConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Birim Dönüştürücü")
        self.geometry("400x400")

        # Başlık
        tk.Label(self, text="Birim Dönüştürücü", font=("Arial", 16)).pack(pady=10)

        # Dönüşüm türü seçimi
        tk.Label(self, text="Dönüşüm Türü:").pack()
        self.conversion_type = ttk.Combobox(self, values=["Uzunluk", "Ağırlık", "Sıcaklık"], state="readonly")
        self.conversion_type.pack(pady=5)
        self.conversion_type.bind("<<ComboboxSelected>>", self.update_units)

        # Giriş birimi seçimi
        tk.Label(self, text="Giriş Birimi:").pack()
        self.input_unit = ttk.Combobox(self, state="readonly")
        self.input_unit.pack(pady=5)

        # Çıkış birimi seçimi
        tk.Label(self, text="Çıkış Birimi:").pack()
        self.output_unit = ttk.Combobox(self, state="readonly")
        self.output_unit.pack(pady=5)

        # Giriş değeri
        tk.Label(self, text="Değer:").pack()
        self.value_entry = tk.Entry(self)
        self.value_entry.pack(pady=5)

        # Sonuç alanı
        self.result_label = tk.Label(self, text="Sonuç: ", font=("Arial", 12))
        self.result_label.pack(pady=10)

        # Dönüştürme butonu
        convert_button = tk.Button(self, text="Dönüştür", command=self.convert)
        convert_button.pack(pady=5)

        # Dönüşüm verileri
        self.conversion_data = {
            "Uzunluk": {
                "metre": 1,
                "kilometre": 0.001,
                "santimetre": 100,
                "mil": 0.000621371,
                "inch": 39.3701
            },
            "Ağırlık": {
                "kilogram": 1,
                "gram": 1000,
                "ton": 0.001,
                "pound": 2.20462,
                "ounce": 35.274
            },
            "Sıcaklık": None  # Özel hesaplama gerektirir
        }

    def update_units(self, event):
        conversion_type = self.conversion_type.get()
        if conversion_type == "Sıcaklık":
            units = ["Celsius", "Fahrenheit", "Kelvin"]
        else:
            units = list(self.conversion_data[conversion_type].keys())

        self.input_unit["values"] = units
        self.output_unit["values"] = units
        self.input_unit.set("")
        self.output_unit.set("")

    def convert(self):
        conversion_type = self.conversion_type.get()
        input_unit = self.input_unit.get()
        output_unit = self.output_unit.get()
        value = self.value_entry.get()

        if not conversion_type or not input_unit or not output_unit or not value:
            self.result_label.config(text="Lütfen tüm alanları doldurun.")
            return

        try:
            value = float(value)
        except ValueError:
            self.result_label.config(text="Lütfen geçerli bir sayı girin.")
            return

        if conversion_type == "Sıcaklık":
            result = self.convert_temperature(value, input_unit, output_unit)
        else:
            result = self.convert_generic(value, input_unit, output_unit, conversion_type)

        self.result_label.config(text=f"Sonuç: {result}")

    def convert_generic(self, value, input_unit, output_unit, conversion_type):
        input_factor = self.conversion_data[conversion_type][input_unit]
        output_factor = self.conversion_data[conversion_type][output_unit]
        return value * (output_factor / input_factor)

    def convert_temperature(self, value, input_unit, output_unit):
        if input_unit == output_unit:
            return value

        # Convert input to Celsius
        if input_unit == "Fahrenheit":
            value = (value - 32) * 5/9
        elif input_unit == "Kelvin":
            value = value - 273.15

        # Convert Celsius to output
        if output_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif output_unit == "Kelvin":
            return value + 273.15
        return value

if __name__ == "__main__":
    app = UnitConverter()
    app.mainloop()

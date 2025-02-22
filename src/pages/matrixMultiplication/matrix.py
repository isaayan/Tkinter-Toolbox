import tkinter as tk
from tkinter import messagebox
import numpy as np

class MatrixMultiplicationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Matris Çarpımı Hesaplayıcı")
        self.geometry("600x600")

        self.create_widgets()

    def create_widgets(self):
        # Matris A Boyutları
        tk.Label(self, text="Matris A Satır Sayısı:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.rows_a_entry = tk.Entry(self)
        self.rows_a_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Matris A Sütun Sayısı:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.cols_a_entry = tk.Entry(self)
        self.cols_a_entry.grid(row=1, column=1, padx=10, pady=5)

        # Matris B Boyutları
        tk.Label(self, text="Matris B Satır Sayısı:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.rows_b_entry = tk.Entry(self)
        self.rows_b_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self, text="Matris B Sütun Sayısı:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.cols_b_entry = tk.Entry(self)
        self.cols_b_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(self, text="Matrisleri Al", command=self.get_matrices).grid(row=4, column=0, columnspan=2, pady=10)

        # Hata ve Bilgi mesajları
        self.message_label = tk.Label(self, text="", fg="red")
        self.message_label.grid(row=5, column=0, columnspan=2)

        # Matris A ve B'nin veri giriş alanları
        self.matrix_a_entries = []
        self.matrix_b_entries = []

        # Sonuç Gösterim Alanı
        self.result_text = tk.Text(self, height=10, width=50)
        self.result_text.grid(row=7, column=0, columnspan=2, pady=10)

    def get_matrices(self):
        # Matris boyutlarını al
        try:
            rows_a = int(self.rows_a_entry.get())
            cols_a = int(self.cols_a_entry.get())
            rows_b = int(self.rows_b_entry.get())
            cols_b = int(self.cols_b_entry.get())

            # Matris boyutlarının uygunluğunu kontrol et
            if cols_a != rows_b:
                self.message_label.config(text="Matris çarpımı için sütun sayısı A'nın satır sayısına eşit olmalı!", fg="red")
                return
            else:
                self.message_label.config(text="", fg="red")

            # Matris A için giriş alanları oluştur
            self.create_matrix_entries(rows_a, cols_a, "A")
            # Matris B için giriş alanları oluştur
            self.create_matrix_entries(rows_b, cols_b, "B")
            
            # Çarpım butonunu göster
            tk.Button(self, text="Matris Çarp", command=lambda: self.multiply_matrices(rows_a, cols_a, rows_b, cols_b)).grid(row=6, column=0, columnspan=2, pady=10)

        except ValueError:
            self.message_label.config(text="Lütfen geçerli sayılar girin!", fg="red")

    def create_matrix_entries(self, rows, cols, matrix_name):
        """
        Dinamik olarak matris için giriş alanları oluşturur.
        """
        entries = []
        for i in range(rows):
            row_entries = []
            for j in range(cols):
                entry = tk.Entry(self)
                entry.grid(row=7 + i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            entries.append(row_entries)
        
        if matrix_name == "A":
            self.matrix_a_entries = entries
        else:
            self.matrix_b_entries = entries

    def multiply_matrices(self, rows_a, cols_a, rows_b, cols_b):
        """
        Matris A ve B'nin çarpımını hesaplar.
        """
        try:
            matrix_a = np.array([[int(self.matrix_a_entries[i][j].get()) for j in range(cols_a)] for i in range(rows_a)])
            matrix_b = np.array([[int(self.matrix_b_entries[i][j].get()) for j in range(cols_b)] for i in range(rows_b)])

            result = np.dot(matrix_a, matrix_b)

            self.show_result(result)
        except ValueError:
            self.message_label.config(text="Matris elemanları sayısal olmalıdır!", fg="red")

    def show_result(self, result):
        """
        Çarpım sonucu olan matrisi gösterir.
        """
        self.result_text.delete(1.0, tk.END)
        rows, cols = result.shape
        for i in range(rows):
            row_text = " ".join(map(str, result[i]))
            self.result_text.insert(tk.END, row_text + "\n")


if __name__ == "__main__":
    app = MatrixMultiplicationApp()
    app.mainloop()

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import os

from src.pages.denklem2.denklem2 import SolverWindow
from src.pages.unitConverter.unitconverter import UnitConverter
from src.pages.calculator.calculator import Calculator
from src.pages.numberGuess.numberGuess import NumberGuess
from src.pages.stockTracking.stockTracking import StockTrackingApp
from src.pages.fibonacciSeries.fibonacci import FibonacciCryptographyApp
from src.pages.library.library import LibraryApp
from src.pages.matrixMultiplication.matrix import MatrixMultiplicationApp
from src.pages.textAnalysis.textAnalysis import TextAnalysisApp
from src.pages.miniGame.miniGame import RockPaperScissorsApp

# Ana dizini belirleme
main_directory = os.path.dirname(os.path.abspath(__file__))

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Birbirinden Farklı 10 Uygulama")
        self.geometry("1250x550")
        self.current_page = None

    def show_page(self, page):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = page
        self.current_page.pack(fill=tk.BOTH, expand=True)

class HomePage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        # Ana çerçeve
        main_frame = tk.Frame(self, padx=20, pady=20)
        main_frame.pack(anchor="center", expand=True)

        # Buton çerçevesi
        button_frame = tk.Frame(main_frame, padx=10, pady=10)
        button_frame.grid(row=0, column=0, padx=20, pady=20)

        # Resim dosyalarını yükleme
        file_names = [f"src\\assets\\{i}.png" for i in range(1, 11)]
        file_directories = [os.path.join(main_directory, file_name) for file_name in file_names]

        self.images = []
        for directory in file_directories:
            if os.path.exists(directory):
                img = Image.open(directory).resize((175, 175))  # Resimleri 175x175 px boyutuna ayarla
                self.images.append(ImageTk.PhotoImage(img))
            else:
                print(f"Uyarı: Resim dosyası bulunamadı - {directory}")
                placeholder = Image.new("RGB", (175, 175), "gray")
                self.images.append(ImageTk.PhotoImage(placeholder))

        # Komutlar
        commands = [
            self.show_sayfa1, self.show_sayfa2, self.show_sayfa3, self.show_sayfa4,
            self.show_sayfa5, self.show_sayfa6, self.show_sayfa7, self.show_sayfa8,
            self.show_sayfa9, self.show_sayfa10,
        ]

        # Butonları grid yöntemiyle düzenle
        for i, (image, command) in enumerate(zip(self.images, commands)):
            row = i // 5  # 0-4 arası butonlar birinci satır, 5-9 arası butonlar ikinci satır
            col = i % 5  # Sütun numarası
            button = tk.Button(button_frame, image=image, command=command)
            button.grid(row=row, column=col, padx=15, pady=15)

    # Sayfa fonksiyonları
    def show_sayfa1(self):
        SolverWindow()

    def show_sayfa2(self):
        UnitConverter()

    def show_sayfa3(self):
        Calculator()

    def show_sayfa4(self):
        NumberGuess()

    def show_sayfa5(self):
        StockTrackingApp()

    def show_sayfa6(self):
        FibonacciCryptographyApp()

    def show_sayfa7(self):
        LibraryApp()

    def show_sayfa8(self):
        MatrixMultiplicationApp()

    def show_sayfa9(self):
        TextAnalysisApp()

    def show_sayfa10(self):
        RockPaperScissorsApp()

if __name__ == "__main__":
    app = Application()
    app.show_page(HomePage(app, app))
    app.mainloop()

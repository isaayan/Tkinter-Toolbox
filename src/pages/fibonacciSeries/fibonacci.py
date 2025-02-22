import tkinter as tk

class FibonacciCryptographyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fibonacci Şifreleme ve Çözme")
        self.geometry("500x400")
        self.resizable(False, False)

        # Arayüz bileşenlerini oluştur
        self.create_widgets()

    def create_widgets(self):
        # Giriş için etiket ve metin kutusu
        tk.Label(self, text="Metin Girin:", font=("Arial", 12)).pack(pady=5)
        self.input_entry = tk.Entry(self, font=("Arial", 12), width=40)
        self.input_entry.pack(pady=5)

        # Şifreleme ve çözme butonları
        tk.Button(self, text="Şifrele", command=self.encrypt_text).pack(pady=10)
        tk.Button(self, text="Çöz", command=self.decrypt_text).pack(pady=10)

        # Sonuç alanı
        tk.Label(self, text="Sonuç:", font=("Arial", 12)).pack(pady=5)
        self.result_label = tk.Label(self, text="", font=("Arial", 12), fg="blue", wraplength=480, justify="center")
        self.result_label.pack(pady=10)

        # Hata mesajları için alan
        self.message_label = tk.Label(self, text="", font=("Arial", 12), fg="red")
        self.message_label.pack(pady=10)

    def fibonacci_series(self, n):
        # İlk n Fibonacci sayısını döndür
        fib = [0, 1]
        for _ in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib

    def encrypt_text(self):
        text = self.input_entry.get()
        if not text:
            self.message_label.config(text="Lütfen bir metin girin.")
            return

        self.message_label.config(text="")
        fib = self.fibonacci_series(len(text))
        encrypted = "".join(chr((ord(char) + fib[i]) % 256) for i, char in enumerate(text))
        self.result_label.config(text=encrypted)

    def decrypt_text(self):
        text = self.input_entry.get()
        if not text:
            self.message_label.config(text="Lütfen bir metin girin.")
            return

        self.message_label.config(text="")
        fib = self.fibonacci_series(len(text))
        decrypted = "".join(chr((ord(char) - fib[i]) % 256) for i, char in enumerate(text))
        self.result_label.config(text=decrypted)

if __name__ == "__main__":
    app = FibonacciCryptographyApp()
    app.mainloop()

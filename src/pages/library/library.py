import tkinter as tk
from tkinter import messagebox

class Library:
    def __init__(self):
        # Kitapları tutacak bir sözlük (dictionary) başlatıyoruz.
        self.books = {}

    def add_book(self, name, author, stock, message_label):
        """
        Yeni bir kitap ekler veya mevcut bir kitabın stok miktarını artırır.
        """
        if name in self.books:
            # Eğer kitap zaten varsa, stok miktarını artırıyoruz.
            self.books[name]['stock'] += stock
            message_label.config(text=f"'{name}' kitabı {stock} adet eklendi.", fg="green")
        else:
            # Yeni bir kitap ekliyoruz.
            self.books[name] = {'author': author, 'stock': stock}
            message_label.config(text=f"'{name}' kitabı eklendi.", fg="green")

    def list_books(self, product_list_text):
        """
        Mevcut tüm kitapları listele.
        """
        product_list_text.delete(1.0, tk.END)
        if self.books:
            for name, details in self.books.items():
                product_list_text.insert(tk.END, f"{name} by {details['author']} - Stok: {details['stock']}\n")
        else:
            product_list_text.insert(tk.END, "Stokta kitap yok.\n")

    def borrow_book(self, name, message_label):
        """
        Kitap ödünç alındığında stok miktarını bir azaltır.
        """
        if name in self.books and self.books[name]['stock'] > 0:
            self.books[name]['stock'] -= 1
            message_label.config(text=f"'{name}' kitabı ödünç alındı.", fg="green")
        else:
            message_label.config(text="Bu kitap mevcut değil ya da stokta kalmadı!", fg="red")

    def return_book(self, name, message_label):
        """
        Kitap iade edildiğinde stok miktarını bir artırır.
        """
        if name in self.books:
            self.books[name]['stock'] += 1
            message_label.config(text=f"'{name}' kitabı iade edildi.", fg="green")
        else:
            message_label.config(text="Bu kitap mevcut değil!", fg="red")

    def get_book_stock(self, name, message_label):
        """
        Belirli bir kitabın stok miktarını döner.
        """
        if name in self.books:
            message_label.config(text=f"'{name}' kitabının stok miktarı: {self.books[name]['stock']}", fg="green")
        else:
            message_label.config(text="Bu kitap mevcut değil!", fg="red")

    def get_low_stock_books(self, product_list_text, threshold=5):
        """
        Düşük stoklu kitapları döner. Varsayılan olarak 5 adet ve daha az olan kitaplar.
        """
        low_stock_books = {name: details for name, details in self.books.items() if details['stock'] <= threshold}
        product_list_text.delete(1.0, tk.END)
        if low_stock_books:
            for name, details in low_stock_books.items():
                product_list_text.insert(tk.END, f"{name} by {details['author']} - Stok: {details['stock']} (Düşük Stok)\n")
        else:
            product_list_text.insert(tk.END, "Düşük stoklu kitap yok.\n")


# GUI Kısımları
class LibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kütüphane Yönetim Sistemi")
        self.geometry("600x500")
        self.library = Library()

        self.create_widgets()

    def create_widgets(self):
        # Kitap Ekleme Bölümü
        tk.Label(self, text="Kitap Adı:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.book_name_entry = tk.Entry(self)
        self.book_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Yazar:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.author_entry = tk.Entry(self)
        self.author_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Stok Miktarı:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.stock_entry = tk.Entry(self)
        self.stock_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self, text="Kitap Ekle", command=self.add_book).grid(row=3, column=0, columnspan=2, pady=10)

        # Mesaj Gösterim Alanı
        self.message_label = tk.Label(self, text="", fg="red")
        self.message_label.grid(row=4, column=0, columnspan=2)

        # Kitap Listeleme Bölümü
        tk.Button(self, text="Kitapları Listele", command=self.list_books).grid(row=5, column=0, columnspan=2, pady=10)

        # Kitap Ödünç Alma Bölümü
        tk.Label(self, text="Ödünç Alınacak Kitap Adı:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.borrow_book_name_entry = tk.Entry(self)
        self.borrow_book_name_entry.grid(row=6, column=1, padx=10, pady=5)

        tk.Button(self, text="Kitap Ödünç Al", command=self.borrow_book).grid(row=7, column=0, columnspan=2, pady=10)

        # Kitap İade Etme Bölümü
        tk.Label(self, text="İade Edilecek Kitap Adı:").grid(row=8, column=0, padx=10, pady=5, sticky="w")
        self.return_book_name_entry = tk.Entry(self)
        self.return_book_name_entry.grid(row=8, column=1, padx=10, pady=5)

        tk.Button(self, text="Kitap İade Et", command=self.return_book).grid(row=9, column=0, columnspan=2, pady=10)

        # Düşük Stok Bölümü
        tk.Button(self, text="Düşük Stoklu Kitaplar", command=self.show_low_stock).grid(row=10, column=0, columnspan=2, pady=10)

        # Kitap Listeleme Alanı
        self.book_list_text = tk.Text(self, height=10, width=50)
        self.book_list_text.grid(row=11, column=0, columnspan=2, pady=10)

    def add_book(self):
        book_name = self.book_name_entry.get().strip()
        author = self.author_entry.get().strip()
        try:
            stock = int(self.stock_entry.get())
            if book_name and author and stock > 0:
                self.library.add_book(book_name, author, stock, self.message_label)
            else:
                self.message_label.config(text="Lütfen geçerli bir kitap adı, yazar ve miktar girin.", fg="red")
        except ValueError:
            self.message_label.config(text="Stok miktarı sayısal bir değer olmalı!", fg="red")

        self.book_name_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.stock_entry.delete(0, tk.END)

    def list_books(self):
        self.library.list_books(self.book_list_text)

    def borrow_book(self):
        book_name = self.borrow_book_name_entry.get().strip()
        if book_name:
            self.library.borrow_book(book_name, self.message_label)
        else:
            self.message_label.config(text="Lütfen ödünç alınacak kitap adını girin.", fg="red")
        self.borrow_book_name_entry.delete(0, tk.END)

    def return_book(self):
        book_name = self.return_book_name_entry.get().strip()
        if book_name:
            self.library.return_book(book_name, self.message_label)
        else:
            self.message_label.config(text="Lütfen iade edilecek kitap adını girin.", fg="red")
        self.return_book_name_entry.delete(0, tk.END)

    def show_low_stock(self):
        self.library.get_low_stock_books(self.book_list_text)

if __name__ == "__main__":
    app = LibraryApp()
    app.mainloop()

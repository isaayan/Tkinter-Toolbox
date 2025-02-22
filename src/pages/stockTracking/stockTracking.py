import tkinter as tk

class StockTrackingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Basit Stok Takip Sistemi")
        self.geometry("600x500")

        self.stock = {}

        self.create_widgets()

    def create_widgets(self):
        # Ürün Ekleme Bölümü
        tk.Label(self, text="Ürün Adı:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.product_name_entry = tk.Entry(self)
        self.product_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Stok Miktarı:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.product_quantity_entry = tk.Entry(self)
        self.product_quantity_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(self, text="Ürün Ekle", command=self.add_product).grid(row=2, column=0, columnspan=2, pady=10)

        # Mesaj Gösterim Alanı
        self.message_label = tk.Label(self, text="", fg="red")
        self.message_label.grid(row=3, column=0, columnspan=2)

        # Ürün Listeleme Bölümü
        tk.Button(self, text="Ürünleri Listele", command=self.list_products).grid(row=4, column=0, columnspan=2, pady=10)

        # Stoktan Çıkarma Bölümü
        tk.Label(self, text="Stoktan Çıkarılacak Ürün Adı:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.remove_product_name_entry = tk.Entry(self)
        self.remove_product_name_entry.grid(row=5, column=1, padx=10, pady=5)

        tk.Label(self, text="Miktar:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.remove_quantity_entry = tk.Entry(self)
        self.remove_quantity_entry.grid(row=6, column=1, padx=10, pady=5)

        tk.Button(self, text="Stoktan Çıkar", command=self.remove_product).grid(row=7, column=0, columnspan=2, pady=10)

        # Düşük Stok Bölümü
        tk.Button(self, text="Düşük Stoklu Ürünler", command=self.show_low_stock).grid(row=8, column=0, columnspan=2, pady=10)

        # Ürün Listeleme Alanı
        self.product_list_text = tk.Text(self, height=10, width=50)
        self.product_list_text.grid(row=9, column=0, columnspan=2, pady=10)

    def add_product(self):
        product_name = self.product_name_entry.get().strip()
        try:
            quantity = int(self.product_quantity_entry.get())
            if product_name and quantity > 0:
                if product_name in self.stock:
                    self.stock[product_name] += quantity
                else:
                    self.stock[product_name] = quantity
                self.message_label.config(text=f"'{product_name}' ürünü eklendi!", fg="green")
            else:
                self.message_label.config(text="Geçerli bir ürün adı ve miktar girin!", fg="red")
        except ValueError:
            self.message_label.config(text="Miktar sayısal bir değer olmalı!", fg="red")

        self.product_name_entry.delete(0, tk.END)
        self.product_quantity_entry.delete(0, tk.END)

    def list_products(self):
        self.product_list_text.delete(1.0, tk.END)
        if self.stock:
            for product, quantity in self.stock.items():
                self.product_list_text.insert(tk.END, f"{product}: {quantity}\n")
        else:
            self.product_list_text.insert(tk.END, "Stokta ürün yok!\n")

    def remove_product(self):
        product_name = self.remove_product_name_entry.get().strip()
        try:
            quantity = int(self.remove_quantity_entry.get())
            if product_name in self.stock and quantity > 0:
                if self.stock[product_name] > quantity:
                    self.stock[product_name] -= quantity
                    self.message_label.config(text=f"'{product_name}' stoktan çıkarıldı!", fg="green")
                elif self.stock[product_name] == quantity:
                    del self.stock[product_name]
                    self.message_label.config(text=f"'{product_name}' stoktan tamamen çıkarıldı!", fg="green")
                else:
                    self.message_label.config(text=f"Stoktaki miktardan fazlasını çıkaramazsınız!", fg="red")
            else:
                self.message_label.config(text="Geçerli bir ürün adı ve miktar girin!", fg="red")
        except ValueError:
            self.message_label.config(text="Miktar sayısal bir değer olmalı!", fg="red")

        self.remove_product_name_entry.delete(0, tk.END)
        self.remove_quantity_entry.delete(0, tk.END)

    def show_low_stock(self):
        self.product_list_text.delete(1.0, tk.END)
        low_stock_products = {product: quantity for product, quantity in self.stock.items() if quantity < 10}
        if low_stock_products:
            for product, quantity in low_stock_products.items():
                self.product_list_text.insert(tk.END, f"{product}: {quantity} (Düşük Stok)\n")
        else:
            self.product_list_text.insert(tk.END, "Düşük stoklu ürün yok!\n")

if __name__ == "__main__":
    app = StockTrackingApp()
    app.mainloop()

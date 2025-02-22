import tkinter as tk
from collections import Counter
import re

class TextAnalysisApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Metin Analiz Programı")
        self.geometry("600x600")
        
        self.create_widgets()

    def create_widgets(self):
        # Metin Girişi Bölümü
        tk.Label(self, text="Metninizi Girin:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.text_entry = tk.Text(self, height=10, width=50)
        self.text_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        # Analiz Butonu
        tk.Button(self, text="Metni Analiz Et", command=self.analyze_text).grid(row=2, column=0, columnspan=2, pady=10)

        # Sonuçlar
        self.result_label = tk.Label(self, text="", justify="left", anchor="w")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def analyze_text(self):
        # Kullanıcıdan alınan metin
        text = self.text_entry.get("1.0", tk.END).strip()

        if not text:
            self.result_label.config(text="Lütfen metin girin!", fg="red")
            return

        # Kelimeleri ayırmak için düzenli ifadeler
        words = re.findall(r'\b\w+\b', text.lower())
        num_words = len(words)

        # Cümle sayısını hesaplamak
        sentences = re.split(r'[.!?]', text)
        num_sentences = len([s for s in sentences if s.strip()])

        # Ortalama kelime uzunluğu hesaplamak
        average_word_length = sum(len(word) for word in words) / num_words if num_words > 0 else 0

        # En sık kullanılan kelimeyi bulmak
        word_counts = Counter(words)
        most_common_word, most_common_count = word_counts.most_common(1)[0] if word_counts else ("", 0)

        # Sonuçları güncelle
        result_text = (
            f"Toplam Kelime Sayısı: {num_words}\n"
            f"En Sık Kullanılan Kelime: '{most_common_word}' ({most_common_count} kez)\n"
            f"Cümle Sayısı: {num_sentences}\n"
            f"Ortalama Kelime Uzunluğu: {average_word_length:.2f} karakter"
        )
        self.result_label.config(text=result_text, fg="black")

if __name__ == "__main__":
    app = TextAnalysisApp()
    app.mainloop()

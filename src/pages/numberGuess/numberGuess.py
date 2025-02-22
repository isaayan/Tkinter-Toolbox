import tkinter as tk
import random

class NumberGuess(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sayı Tahmin Oyunu")
        self.geometry("400x300")
        self.resizable(False, False)
        self.random_number = None
        self.attempts = 0
        self.max_number = 100

        self.create_widgets()

    def create_widgets(self):
        # Zorluk Seçimi
        tk.Label(self, text="Zorluk Seviyesi Seçin:", font=("Arial", 14)).pack(pady=10)
        difficulty_frame = tk.Frame(self)
        difficulty_frame.pack()
        tk.Button(difficulty_frame, text="Kolay (1-50)", command=lambda: self.set_difficulty(50)).pack(side=tk.LEFT, padx=10)
        tk.Button(difficulty_frame, text="Orta (1-100)", command=lambda: self.set_difficulty(100)).pack(side=tk.LEFT, padx=10)
        tk.Button(difficulty_frame, text="Zor (1-200)", command=lambda: self.set_difficulty(200)).pack(side=tk.LEFT, padx=10)

        # Tahmin Arayüzü
        self.game_frame = tk.Frame(self)
        
        self.guess_entry = tk.Entry(self.game_frame, font=("Arial", 14))
        self.guess_entry.pack(pady=5)
        tk.Button(self.game_frame, text="Tahmin Et", command=self.check_guess).pack(pady=5)

        self.result_label = tk.Label(self.game_frame, text="", font=("Arial", 12), fg="red")
        self.result_label.pack(pady=5)

    def set_difficulty(self, max_number):
        self.max_number = max_number
        self.random_number = random.randint(1, self.max_number)
        self.attempts = 0
        self.result_label.config(text=f"1 ile {self.max_number} arasında bir sayı tahmin edin!")
        self.game_frame.pack(fill=tk.BOTH, expand=True)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1

            if guess < 1 or guess > self.max_number:
                self.result_label.config(text=f"Lütfen 1 ile {self.max_number} arasında bir sayı girin.")
            elif guess < self.random_number:
                self.result_label.config(text="Daha büyük bir sayı söyleyin.")
            elif guess > self.random_number:
                self.result_label.config(text="Daha küçük bir sayı söyleyin.")
            else:
                self.result_label.config(text=f"Tebrikler! {self.attempts} denemede doğru tahmin ettiniz.")
                self.reset_game()
        except ValueError:
            self.result_label.config(text="Lütfen geçerli bir sayı girin.")

        self.guess_entry.delete(0, tk.END)

    def reset_game(self):
        self.random_number = random.randint(1, self.max_number)
        self.attempts = 0
        self.result_label.config(text=f"1 ile {self.max_number} arasında yeni bir sayı tahmin edin!")

if __name__ == "__main__":
    app = NumberGuess()
    app.mainloop()

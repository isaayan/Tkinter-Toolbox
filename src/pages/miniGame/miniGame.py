import tkinter as tk
import random

class RockPaperScissorsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Taş, Kağıt, Makas")
        self.geometry("400x400")
        
        self.player_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        # Başlık
        self.title_label = tk.Label(self, text="Taş, Kağıt, Makas", font=("Arial", 16))
        self.title_label.pack(pady=20)

        # Sonuç Label
        self.result_label = tk.Label(self, text="Sonuç: -", font=("Arial", 14))
        self.result_label.pack(pady=10)

        # Skorlar
        self.score_label = tk.Label(self, text=f"Player: {self.player_score} - Computer: {self.computer_score}", font=("Arial", 12))
        self.score_label.pack(pady=10)

        # Butonlar
        self.rock_button = tk.Button(self, text="Taş", command=lambda: self.play_game("Taş"))
        self.rock_button.pack(side=tk.LEFT, padx=20, pady=10)

        self.paper_button = tk.Button(self, text="Kağıt", command=lambda: self.play_game("Kağıt"))
        self.paper_button.pack(side=tk.LEFT, padx=20, pady=10)

        self.scissors_button = tk.Button(self, text="Makas", command=lambda: self.play_game("Makas"))
        self.scissors_button.pack(side=tk.LEFT, padx=20, pady=10)

        # Yeniden Başlat Butonu
        self.reset_button = tk.Button(self, text="Yeniden Başlat", command=self.reset_game)
        self.reset_button.pack(pady=20)

    def play_game(self, player_choice):
        # Bilgisayarın seçim yapması
        choices = ["Taş", "Kağıt", "Makas"]
        computer_choice = random.choice(choices)

        # Sonucu belirleme
        if player_choice == computer_choice:
            result = "Beraberlik!"
        elif (player_choice == "Taş" and computer_choice == "Makas") or \
             (player_choice == "Kağıt" and computer_choice == "Taş") or \
             (player_choice == "Makas" and computer_choice == "Kağıt"):
            result = f"Başardınız! Bilgisayar {computer_choice} seçti. Kazandınız!"
            self.player_score += 1
        else:
            result = f"Üzgünüz, Bilgisayar {computer_choice} seçti. Kaybettiniz!"
            self.computer_score += 1

        # Sonuç ve skorları güncelleme
        self.result_label.config(text=result)
        self.score_label.config(text=f"Player: {self.player_score} - Computer: {self.computer_score}")

    def reset_game(self):
        # Skorları sıfırlama
        self.player_score = 0
        self.computer_score = 0
        self.result_label.config(text="Sonuç: -")
        self.score_label.config(text=f"Player: {self.player_score} - Computer: {self.computer_score}")

if __name__ == "__main__":
    app = RockPaperScissorsApp()
    app.mainloop()

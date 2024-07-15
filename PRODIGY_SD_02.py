import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")
        
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        
        self.label = tk.Label(root, text="Guess the number (between 1 and 100):")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)
        
        self.button = tk.Button(root, text="Submit", command=self.check_guess)
        self.button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            
            if guess < self.number_to_guess:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text=f"Congratulations! You've guessed it in {self.attempts} attempts.")
                self.play_again()
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

    def play_again(self):
        if messagebox.askyesno("Play Again", "Would you like to play again?"):
            self.number_to_guess = random.randint(1, 100)
            self.attempts = 0
            self.result_label.config(text="")
            self.entry.delete(0, tk.END)
        else:
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()

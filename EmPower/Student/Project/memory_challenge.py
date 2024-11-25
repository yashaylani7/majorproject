import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random


class MemoryChallenge:
    def __init__(self, root):
        self.root = root
        self.root.title("Card Flipping Game")
        self.root.geometry("600x500")

        # List of images to be used for the cards (6 pairs of unique images)
        self.images = [f"../img/{i}.png" for i in range(1, 7)] * 2  # 6 unique pairs
        random.shuffle(self.images)

        self.cards = []
        self.flipped_cards = []
        self.matches = 0
        self.tries = 0
        self.score = 0
        self.score_callback = None  # Callback to send score to the main launcher

        self.create_widgets()

    def set_score_callback(self, callback):
        """Set the callback function to update the score in the main launcher."""
        self.score_callback = callback

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        # Load the card back image (cover)
        self.cover_img = ImageTk.PhotoImage(Image.open("../img/card_back.jpeg").resize((100, 100)))

        # Create 12 cards (buttons) in a 3x4 grid
        for i in range(3):  # 3 rows
            for j in range(4):  # 4 columns
                card = tk.Button(self.frame, image=self.cover_img,
                                 command=lambda idx=len(self.cards): self.flip_card(idx))
                card.grid(row=i, column=j, padx=10, pady=10)
                self.cards.append(card)

        # Labels to show tries, matches, and score
        self.tries_label = tk.Label(self.root, text="Tries: 0", font=("Arial", 14))
        self.tries_label.pack(pady=5)

        self.matches_label = tk.Label(self.root, text="Matches: 0", font=("Arial", 14))
        self.matches_label.pack(pady=5)

        self.score_label = tk.Label(self.root, text="Score: 0", font=("Arial", 14))
        self.score_label.pack(pady=5)

    def flip_card(self, index):
        # Don't allow more than two cards to be flipped at once
        if len(self.flipped_cards) == 2:
            return

        # Load and display the image on the card
        img = ImageTk.PhotoImage(Image.open(self.images[index]).resize((100, 100)))
        self.cards[index].config(image=img)
        self.cards[index].image = img
        self.cards[index].config(state="disabled")  # Disable the card once it's flipped
        self.flipped_cards.append(index)

        # Check if two cards are flipped
        if len(self.flipped_cards) == 2:
            self.root.after(1000, self.check_match)  # Wait 1 second to flip back if no match

    def check_match(self):
        idx1, idx2 = self.flipped_cards
        if self.images[idx1] == self.images[idx2]:
            self.matches += 1
            self.score += 10  # Add 10 points for a correct match
            self.matches_label.config(text=f"Matches: {self.matches}")
            self.score_label.config(text=f"Score: {self.score}")
            if self.score_callback:
                self.score_callback("Memory Challenge", self.score)  # Update score in the main launcher
        else:
            # Flip the cards back to cover if they don't match
            self.score -= 2  # Deduct 2 points for an incorrect match
            self.root.after(500, self.flip_back, idx1, idx2)
            self.score_label.config(text=f"Score: {self.score}")

        self.flipped_cards = []
        self.tries += 1
        self.tries_label.config(text=f"Tries: {self.tries}")

        # Check for game over
        if self.matches == len(self.images) // 2:
            messagebox.showinfo("Game Over", f"You won in {self.tries} tries!\nFinal Score: {self.score}")
            if self.score_callback:
                self.score_callback("Memory Challenge", self.score)  # Final score update

    def flip_back(self, idx1, idx2):
        self.cards[idx1].config(image=self.cover_img, state="normal")
        self.cards[idx2].config(image=self.cover_img, state="normal")


# Launcher to open MemoryChallenge in a new window
def launch_memory_game():
    memory_window = tk.Toplevel(root)
    memory_game = MemoryChallenge(memory_window)

    # Example callback to handle scores (in a real launcher, integrate it dynamically)
    def update_score(game_name, score):
        print(f"Game: {game_name}, Score: {score}")

    memory_game.set_score_callback(update_score)


# Main Game Launcher Window
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Game Launcher")
    root.geometry("500x300")

    # Button to launch the memory game
    memory_button = tk.Button(root, text="Start Memory Challenge", font=("Arial", 16), command=launch_memory_game)
    memory_button.pack(pady=20)

    # Exit Button
    exit_button = tk.Button(root, text="Exit", font=("Arial", 16), command=root.quit)
    exit_button.pack(pady=20)

    root.mainloop()

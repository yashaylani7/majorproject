import tkinter as tk
import random
import time


class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("500x400")
        self.root.configure(bg="#ffccbc")

        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "Practice makes perfect.",
            "Typing speed is an art.",
            "Code is poetry.",
        ]
        self.target_text = random.choice(self.sentences)

        self.game_name = "Typing Speed Test"  # Used for score tracking
        self.start_time = None
        self.score_callback = None

        tk.Label(self.root, text="Type the sentence below:", font=("Arial", 18), bg="#ffccbc").pack(pady=20)

        self.target_label = tk.Label(self.root, text=self.target_text, font=("Arial", 14), bg="#ffccbc", wraplength=450)
        self.target_label.pack(pady=10)

        self.input_entry = tk.Entry(self.root, font=("Arial", 14), width=50)
        self.input_entry.pack(pady=10)
        self.input_entry.bind("<KeyPress>", self.start_timer)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14), bg="#ffccbc")
        self.result_label.pack(pady=10)

        self.time_label = tk.Label(self.root, text="Time: 0.0s", font=("Arial", 14), bg="#ffccbc")
        self.time_label.pack(pady=10)

        tk.Button(
            self.root, text="Check", font=("Arial", 14), command=self.check_typing, bg="#ff7043"
        ).pack(pady=10)

        tk.Button(
            self.root, text="Close", font=("Arial", 14), command=self.close_game, bg="#d32f2f"
        ).pack(pady=10)

    def start_timer(self, event):
        """Start the timer on the first key press."""
        if self.start_time is None:
            self.start_time = time.time()

    def check_typing(self):
        """Check if the entered text matches the target and update the score."""
        user_text = self.input_entry.get()
        if user_text == self.target_text:
            end_time = time.time()
            elapsed_time = round(end_time - self.start_time, 2)
            self.result_label.config(text="Correct! Good job!", fg="green")
            self.time_label.config(text=f"Time: {elapsed_time}s")
            if self.score_callback:
                self.score_callback(self.game_name, int(100 / elapsed_time))  # Calculate score
            self.start_new_round()
        else:
            self.result_label.config(text="Incorrect! Try again.", fg="red")

    def start_new_round(self):
        """Reset for a new typing challenge."""
        self.target_text = random.choice(self.sentences)
        self.target_label.config(text=self.target_text)
        self.input_entry.delete(0, tk.END)
        self.start_time = None

    def close_game(self):
        """Close the game window."""
        self.root.destroy()

    def set_score_callback(self, callback):
        """Set the callback function for updating scores."""
        self.score_callback = callback

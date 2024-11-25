import tkinter as tk
import random


class MathChallenge:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="#ffeb3b")
        self.score = 0
        self.score_callback = None  # Callback to update score in GameLauncher

        # UI Elements
        tk.Label(self.root, text="Solve the math problem!", font=("Arial", 18), bg="#ffeb3b").pack(pady=20)

        self.problem_label = tk.Label(self.root, text="", font=("Arial", 18), bg="#ffeb3b")
        self.problem_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.root, font=("Arial", 18))
        self.answer_entry.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14), bg="#ffeb3b")
        self.result_label.pack(pady=10)

        self.generate_problem()

        tk.Button(
            self.root, text="Check Answer", font=("Arial", 14), command=self.check_answer, bg="#cddc39"
        ).pack(pady=10)

        tk.Button(
            self.root, text="Close", font=("Arial", 14), command=self.close_window, bg="#f44336"
        ).pack(pady=10)

    def set_score_callback(self, callback):
        """Set the score callback to update the score in GameLauncher."""
        self.score_callback = callback

    def generate_problem(self):
        """Generate a new math problem and display it."""
        self.num1 = random.randint(1, 20)
        self.num2 = random.randint(1, 20)
        self.operator = random.choice(["+", "-", "*"])
        self.solution = eval(f"{self.num1} {self.operator} {self.num2}")
        self.problem_label.config(text=f"{self.num1} {self.operator} {self.num2}")
        self.answer_entry.delete(0, tk.END)  # Clear the input field

    def check_answer(self):
        """Check the user's answer and generate a new problem if correct."""
        user_input = self.answer_entry.get()
        try:
            if int(user_input) == self.solution:
                self.result_label.config(text="Correct! Generating next problem...", fg="green")
                self.score += 1
                if self.score_callback:
                    self.score_callback("Math Challenge", self.score)
                self.root.after(1000, self.generate_problem)  # Delay to show "Correct!" before next problem
            else:
                self.result_label.config(text="Wrong! Try Again.", fg="red")
        except ValueError:
            self.result_label.config(text="Invalid Input. Please enter a number.", fg="red")

    def close_window(self):
        """Close the game window."""
        self.root.destroy()

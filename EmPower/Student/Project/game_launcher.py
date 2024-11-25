import tkinter as tk
from tkinter import messagebox
import json
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Import game modules
from sequencing_game import SequencingGame  # Import the Sequencing Game
from math_challenge import MathChallenge
from typing_speed_test import TypingSpeedTest
from memory_challenge import MemoryChallenge
from trivia_quiz import TriviaQuiz


class GameLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 AutismX 🎮")
        self.root.geometry("800x500")
        self.root.configure(bg="#e0f7fa")

        # Ensure scores file exists and load scores
        self.ensure_scores_file()
        self.scores = self.load_scores()

        # Track open game windows by name
        self.open_game_windows = {}

        # Title
        self.title_label = tk.Label(
            root, text="🎮 AutismX 🎮", font=("Arial", 24, "bold"), bg="#00796b", fg="white"
        )
        self.title_label.pack(fill="x", pady=10)

        # Instruction Label
        self.instruction_label = tk.Label(
            root,
            text="Choose a game below to boost your productivity and have fun!",
            font=("Arial", 14),
            bg="#e0f7fa",
            fg="#004d40",
        )
        self.instruction_label.pack(pady=20)

        # Buttons for Games
        self.button_frame = tk.Frame(root, bg="#e0f7fa")
        self.button_frame.pack(pady=20)

        # Buttons for each game
        self.create_game_buttons()

        # Button to show scores
        self.display_scores_button = tk.Button(
            root, text="Show Scores", font=("Arial", 16), command=self.display_scores
        )
        self.display_scores_button.pack(pady=10)

        # Button to display score graph
        self.display_graph_button = tk.Button(
            root, text="Show Scores Graph", font=("Arial", 16), command=self.display_scores_graph
        )
        self.display_graph_button.pack(pady=10)

        # Exit Button
        tk.Button(
            root,
            text="Exit",
            font=("Arial", 16),
            bg="#ff8a80",
            command=root.quit,
            width=15,
        ).pack(pady=20)

    def ensure_scores_file(self):
        """Ensure that the scores.json file exists."""
        if not os.path.exists("scores.json"):
            with open("scores.json", "w") as f:
                json.dump(
                    {
                        "Math Challenge": 0,
                        "Typing Speed Test": 0,
                        "Memory Challenge": 0,
                        "Trivia Quiz": 0,
                        "Sequencing Game": 0,
                    },
                    f,
                )

    def load_scores(self):
        """Load scores from a JSON file (persistent storage)."""
        try:
            with open("scores.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "Math Challenge": 0,
                "Typing Speed Test": 0,
                "Memory Challenge": 0,
                "Trivia Quiz": 0,
                "Sequencing Game": 0,
            }

    def update_score(self, game_name, score):
        """Update the score for a specific game."""
        self.scores[game_name] = score
        with open("scores.json", "w") as f:
            json.dump(self.scores, f)
        print(f"Updated {game_name} score: {score}")

    def create_game_buttons(self):
        """Create buttons for each game."""
        tk.Button(
            self.button_frame,
            text="Math Challenge",
            font=("Arial", 16),
            bg="#80deea",
            command=lambda: self.open_game("Math Challenge", MathChallenge),
            width=15,
        ).grid(row=0, column=0, padx=10, pady=10)

        tk.Button(
            self.button_frame,
            text="Typing Speed Test",
            font=("Arial", 16),
            bg="#80cbc4",
            command=lambda: self.open_game("Typing Speed Test", TypingSpeedTest),
            width=15,
        ).grid(row=0, column=1, padx=10, pady=10)

        tk.Button(
            self.button_frame,
            text="Memory Challenge",
            font=("Arial", 16),
            bg="#b2dfdb",
            command=lambda: self.open_game("Memory Challenge", MemoryChallenge),
            width=15,
        ).grid(row=0, column=2, padx=10, pady=10)

        tk.Button(
            self.button_frame,
            text="Trivia Quiz",
            font=("Arial", 16),
            bg="#aed581",
            command=lambda: self.open_game("Trivia Quiz", TriviaQuiz),
            width=15,
        ).grid(row=0, column=3, padx=10, pady=10)

        tk.Button(
            self.button_frame,
            text="Sequencing Game",
            font=("Arial", 16),
            bg="#ffab91",
            command=lambda: self.open_game("Sequencing Game", SequencingGame),
            width=15,
        ).grid(row=1, column=0, padx=10, pady=10)

    def open_game(self, game_name, game_class):
        """Open a game and pass the game name for score tracking."""
        # Check if the game window is already open
        if game_name not in self.open_game_windows:
            game_window = tk.Toplevel(self.root)
            game_window.title(game_name)
            game_window.geometry("500x400")
            game_instance = game_class(game_window)
            game_instance.game_name = game_name
            game_instance.set_score_callback(self.update_score)
            # Store reference of game window in the dictionary
            self.open_game_windows[game_name] = game_window

            # Bind the close event to remove the window from tracking
            game_window.protocol(
                "WM_DELETE_WINDOW",
                lambda: self.close_game_window(game_name, game_window),
            )
        else:
            # If the window is already open, focus the window
            game_window = self.open_game_windows[game_name]
            game_window.lift()  # Bring the window to the front
            game_window.focus_force()  # Force focus on the window

    def close_game_window(self, game_name, window):
        """Remove the game window from tracking on close."""
        if game_name in self.open_game_windows:
            del self.open_game_windows[game_name]
        window.destroy()

    def display_scores(self):
        """Display all scores in a message box or text label."""
        score_text = "\n".join([f"{game}: {score}" for game, score in self.scores.items()])
        messagebox.showinfo("Scores", score_text)

    def display_scores_graph(self):
        """Display a graph of the scores."""
        games = list(self.scores.keys())
        scores = list(self.scores.values())

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(games, scores, color=['#80deea', '#80cbc4', '#b2dfdb', '#aed581', '#ffab91'])
        ax.set_title("Scores Overview")
        ax.set_xlabel("Games")
        ax.set_ylabel("Scores")

        # Create a new window for the graph
        graph_window = tk.Toplevel(self.root)
        graph_window.title("Scores Graph")

        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Close button
        tk.Button(graph_window, text="Close", command=graph_window.destroy).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = GameLauncher(root)
    root.mainloop()

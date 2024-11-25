import tkinter as tk
from tkinter import messagebox
import random

class SequencingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Sequencing Game")
        self.root.geometry("600x450")
        self.root.configure(bg="#e8f5e9")

        # Initialize variables
        self.sequence = []  # Correct sequence
        self.player_sequence = []  # Player's attempted sequence
        self.dragging_item = None  # Item currently being dragged
        self.difficulty = 4  # Default number of items in sequence
        self.score = 0  # Initialize score

        # Title
        tk.Label(
            self.root,
            text="🧩 Sequencing Game for Cognitive Development 🧩",
            font=("Arial", 16, "bold"),
            bg="#43a047",
            fg="white",
        ).pack(pady=10)

        # Instruction Label
        tk.Label(
            self.root,
            text="Drag and drop the items to arrange them in the correct order.",
            font=("Arial", 12),
            bg="#e8f5e9",
            fg="#1b5e20",
        ).pack(pady=5)

        # Game Frame
        self.game_frame = tk.Frame(self.root, bg="#e8f5e9")
        self.game_frame.pack(pady=20)

        # Drop Area (for the sequence display)
        self.drop_area = tk.Frame(self.game_frame, bg="#e0e0e0", relief="sunken", height=80, width=500)
        self.drop_area.pack_propagate(False)
        self.drop_area.pack(pady=20)

        # Buttons
        tk.Button(
            self.root, text="Start New Game", font=("Arial", 14), command=self.start_game, bg="#81c784"
        ).pack(pady=10)

        tk.Button(
            self.root, text="Exit", font=("Arial", 14), command=root.quit, bg="#e57373"
        ).pack(pady=10)

        # Score Label
        self.score_label = tk.Label(
            self.root, text=f"Score: {self.score}", font=("Arial", 14), bg="#e8f5e9", fg="#1b5e20"
        )
        self.score_label.pack(pady=10)

        self.start_game()

    def start_game(self):
        """Start a new game with a random sequence."""
        self.sequence = self.generate_sequence(self.difficulty)
        self.player_sequence = []

        # Clear the game frame
        for widget in self.game_frame.winfo_children():
            widget.destroy()

        # Recreate the drop area
        self.drop_area = tk.Frame(self.game_frame, bg="#e0e0e0", relief="sunken", height=80, width=500)
        self.drop_area.pack_propagate(False)
        self.drop_area.pack(pady=20)

        # Display shuffled items
        shuffled_items = self.sequence.copy()
        random.shuffle(shuffled_items)

        for item in shuffled_items:
            label = tk.Label(
                self.game_frame,
                text=item,
                font=("Arial", 16),
                bg="#ffcc80",
                relief="raised",
                padx=10,
                pady=5,
            )
            label.bind("<Button-1>", self.start_drag)
            label.bind("<B1-Motion>", self.do_drag)
            label.bind("<ButtonRelease-1>", self.stop_drag)
            label.pack(side="left", padx=5, pady=10)

    def generate_sequence(self, length):
        """Generate a simple sequential pattern for the game."""
        return [f"Step {i}" for i in range(1, length + 1)]

    def start_drag(self, event):
        """Start dragging an item."""
        self.dragging_item = event.widget
        self.dragging_item.lift()

    def do_drag(self, event):
        """Move the dragged item."""
        if self.dragging_item:
            self.dragging_item.place(x=event.x_root - self.game_frame.winfo_rootx(),
                                     y=event.y_root - self.game_frame.winfo_rooty())

    def stop_drag(self, event):
        """Drop the dragged item in the drop area."""
        if self.dragging_item:
            # Check if dropped inside the drop area
            if self.is_inside_drop_area(event):
                # Add the dragged item to the player's sequence
                self.player_sequence.append(self.dragging_item.cget("text"))

                # Update the drop area to show the sequence
                self.update_drop_area()

                # Destroy the dragged item
                self.dragging_item.destroy()

                # Check if the sequence is complete
                if len(self.player_sequence) == len(self.sequence):
                    self.check_sequence()
            else:
                # Reset position if not dropped in the area
                self.dragging_item.place_forget()

            self.dragging_item = None

    def is_inside_drop_area(self, event):
        """Check if the current position is inside the drop area."""
        x, y = event.x_root, event.y_root
        x1, y1 = self.drop_area.winfo_rootx(), self.drop_area.winfo_rooty()
        x2, y2 = x1 + self.drop_area.winfo_width(), y1 + self.drop_area.winfo_height()
        return x1 <= x <= x2 and y1 <= y <= y2

    def update_drop_area(self):
        """Update the drop area to display the player's sequence."""
        for widget in self.drop_area.winfo_children():
            widget.destroy()  # Clear the drop area

        for step in self.player_sequence:
            label = tk.Label(
                self.drop_area,
                text=step,
                font=("Arial", 14),
                bg="#a5d6a7",
                relief="groove",
                padx=5,
                pady=5,
            )
            label.pack(side="left", padx=5)

    def check_sequence(self):
        """Check if the player's sequence matches the correct sequence."""
        if self.player_sequence == self.sequence:
            self.score += 10  # Add points for a correct sequence
            messagebox.showinfo("Success!", "🎉 Great job! You arranged the sequence correctly!")
        else:
            self.score -= 5  # Deduct points for an incorrect sequence
            messagebox.showerror("Try Again", "Oops! The sequence is incorrect. Try again!")

        self.update_score_label()
        self.start_game()

    def update_score_label(self):
        """Update the score label to display the current score."""
        self.score_label.config(text=f"Score: {self.score}")

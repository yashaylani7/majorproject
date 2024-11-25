import tkinter as tk

class TriviaQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Trivia Quiz")
        self.root.geometry("500x400")
        self.root.configure(bg="lightblue")

        # Questions and Answers
        self.questions = [
            {
                "question": "When you are hungry, what should you do?",
                "options": ["Ask for food", "Go to bed", "Drink water", "Play with toys"],
                "answer": "Ask for food",
            },
            {
                "question": "What do you say when you need help?",
                "options": ["I’m done", "Stop", "Please help me", "No thank you"],
                "answer": "Please help me",
            },
            {
                "question": "When it's time to brush your teeth, what do you use?",
                "options": ["A towel", "Toothbrush and toothpaste", "A spoon", "Soap"],
                "answer": "Toothbrush and toothpaste",
            },
        ]

        self.current_question = 0
        self.score = 0
        self.score_callback = None  # Placeholder for the score callback function

        self.create_widgets()

    def set_score_callback(self, callback):
        """Set the callback function to update the score in the main game hub."""
        self.score_callback = callback

    def create_widgets(self):
        # Create a frame for the quiz
        self.quiz_frame = tk.Frame(self.root, bg="lightblue", bd=2, relief="solid")
        self.quiz_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Question Label
        self.question_label = tk.Label(
            self.quiz_frame,
            text=self.questions[self.current_question]["question"],
            wraplength=450,
            font=("Arial", 16),
            bg="lightblue",
        )
        self.question_label.pack(pady=20)

        # Options
        self.options_var = tk.StringVar()
        self.option_buttons = []
        for option in self.questions[self.current_question]["options"]:
            rb = tk.Radiobutton(
                self.quiz_frame,
                text=option,
                variable=self.options_var,
                value=option,
                font=("Arial", 14),
                bg="lightblue",
                anchor="w",
            )
            rb.pack(anchor="w", padx=20)
            self.option_buttons.append(rb)

        # Submit Button
        self.submit_button = tk.Button(
            self.quiz_frame,
            text="Submit",
            command=self.check_answer,
            font=("Arial", 14),
            bg="lightgreen",
        )
        self.submit_button.pack(pady=20)

        # Result Label
        self.result_label = tk.Label(
            self.quiz_frame, text="", font=("Arial", 14), bg="lightblue"
        )
        self.result_label.pack(pady=10)

    def check_answer(self):
        selected_option = self.options_var.get()
        correct_answer = self.questions[self.current_question]["answer"]

        if selected_option == correct_answer:
            self.score += 1
            self.result_label.config(text="Correct! 🎉", fg="green")
            if self.score_callback:
                self.score_callback("Trivia Quiz", self.score)  # Update score in the main game hub
        else:
            self.result_label.config(
                text=f"Wrong! The correct answer is: {correct_answer}", fg="red"
            )

        self.current_question += 1

        # Delay before loading the next question
        self.root.after(1500, self.load_next_question)

    def load_next_question(self):
        """Loads the next question and updates the options."""
        if self.current_question < len(self.questions):
            self.question_label.config(
                text=self.questions[self.current_question]["question"]
            )
            self.options_var.set(None)  # Reset the selected option

            for rb in self.option_buttons:
                rb.destroy()  # Remove previous options

            self.option_buttons = []
            for option in self.questions[self.current_question]["options"]:
                rb = tk.Radiobutton(
                    self.quiz_frame,
                    text=option,
                    variable=self.options_var,
                    value=option,
                    font=("Arial", 14),
                    bg="lightblue",
                    anchor="w",
                )
                rb.pack(anchor="w", padx=20)
                self.option_buttons.append(rb)

            self.result_label.config(text="")  # Clear the result
        else:
            self.show_final_score()

    def show_final_score(self):
        """Displays the final score in a new screen-like interface."""
        for widget in self.quiz_frame.winfo_children():
            widget.destroy()  # Remove all widgets from the frame

        # Display final score
        final_score_label = tk.Label(
            self.quiz_frame,
            text=f"Quiz Over!\nYour Final Score: {self.score} / {len(self.questions)}",
            font=("Arial", 18),
            bg="lightblue",
            fg="blue",
        )
        final_score_label.pack(pady=50)

        # Call the score callback function
        if self.score_callback:
            self.score_callback("Trivia Quiz", self.score)  # Final score update

        # Exit Button
        exit_button = tk.Button(
            self.quiz_frame,
            text="Exit",
            command=self.root.destroy,
            font=("Arial", 14),
            bg="red",
            fg="white",
        )
        exit_button.pack(pady=20)

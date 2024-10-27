import tkinter as tk

class ColorblindTest(tk.Frame):
    def __init__(self, master, screen_manager):
        super().__init__(master)
        self.user_answers = None
        self.screen_manager = screen_manager
        self.place(relx=0.5, rely=0.5, anchor="center")

        self.create_widgets()

    def start(self):
        print("Show colour blind screen")

    def create_widgets(self):
        title_label = tk.Label(self, text="Colorblind Test", font=("Helvetica", 18))
        title_label.pack(pady=10)

        # Image display area
        self.logo_image = tk.PhotoImage(file="plate1.png")
        logo_label = tk.Label(self, image=self.logo_image)
        logo_label.pack(pady=20)

        # Input for user response
        self.answer_label = tk.Label(self, text="Enter the number you see:")
        self.answer_label.pack()
        self.answer_entry = tk.Entry(self)
        self.answer_entry.pack()

        # Button to submit answer
        self.submit_button = tk.Button(self, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        # Feedback text
        self.feedback_label = tk.Label(self, text="", font=("Helvetica", 14), fg="red")
        self.feedback_label.pack(pady=10)

    def check_answer(self):
        """Check the user's answer and proceed to the next test."""
        user_answer = self.answer_entry.get().strip()
        correct_answer = 16

        if user_answer == correct_answer:
            self.feedback_label.config(
                text="Colorblindness detected. Adjusting experiment settings."
            )
        else:
            self.feedback_label.config(
                text="No colorblindness detected. Proceeding to experiment."
            )

        self.screen_manager.show_screen("Experiment")

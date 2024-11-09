import tkinter as tk
import settings
from pythonProject.settings import COLOUR_BLIND_MODE


class ColorblindTest(tk.Frame):
    def __init__(self, master, screen_manager):
        super().__init__(master)
        self.screen_manager = screen_manager
        self.place(relx=0.5, rely=0.5, anchor="center")

        self.test_number = 0
        self.images = ["plate1.png", "plate2.png"]  # List of test images
        self.answers = ["15", "12"]  # Correct answers for each test image
        self.user_responses = []  # Stores user's answers for each test
        self.colour_blind = False

        self.create_widgets()

    def start(self):
        self.test_number = 0
        self.user_responses.clear()
        self.colour_blind = False
        self.load_test_image()

    def create_widgets(self):
        title_label = tk.Label(self, text="Colorblind Test", font=("Helvetica", 18))
        title_label.pack(pady=10)

        # Color-blind test image
        self.test_image = tk.PhotoImage(file=self.images[self.test_number])
        self.image_label = tk.Label(self, image=self.test_image)
        self.image_label.pack(pady=20)

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

    def load_test_image(self):
        # Load the next test image based on the test number.
        self.test_image.config(file=self.images[self.test_number])
        self.image_label.config(image=self.test_image)
        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text="")

    def check_answer(self):
        # Check the user's answer and proceed to the next test or finish.
        user_answer = self.answer_entry.get().strip()
        correct_answer = self.answers[self.test_number]

        # Record user response
        self.user_responses.append(user_answer)

        # Check if answer is incorrect for colorblindness detection
        if user_answer != correct_answer:
            self.colour_blind = True

        # Move to the next test or finish
        if self.test_number < len(self.images) - 1:
            self.test_number += 1
            self.load_test_image()
        else:
            # Show feedback after the last test
            if self.colour_blind:
                self.feedback_label.config(
                    text="Colorblindness detected. Adjusting experiment settings."
                )
                settings.COLOUR_BLIND_MODE = True
            else:
                self.feedback_label.config(
                    text="No colorblindness detected. Proceeding to experiment."
                )
                settings.COLOUR_BLIND_MODE = False

            # Proceed to the next screen after a delay to show feedback
            self.after(2000, lambda: self.screen_manager.show_screen("Experiment"))

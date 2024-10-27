import tkinter as tk
from ctypes import c_wchar


class MainMenu(tk.Frame):
    def __init__(self, master, screen_manager):
        super().__init__(master)
        self.logo_image = None
        self.screen_manager = screen_manager
        self.create_widgets()
        self.place(relx=0.5, rely=0.5, anchor="center")

    def start(self):
        print("Show main menu")

    def create_widgets(self):

        self.logo_image = tk.PhotoImage(file="logo.png")
        logo_label = tk.Label(self, image=self.logo_image)
        logo_label.pack(pady=20)
        
        # Menu buttons
        button_new_experiment = tk.Button(self, text="New Experiment", font=("Helvetica", 16),
                                          command=lambda: self.screen_manager.show_screen("ColorblindTest"))
        button_new_experiment.pack(pady=10)

        button_options = tk.Button(self, text="Options", font=("Helvetica", 16),
                                   command=lambda: self.screen_manager.show_screen("Options"))
        button_options.pack(pady=10)

        button_quit = tk.Button(self, text="Quit", font=("Helvetica", 16),
                                command=self.screen_manager.exit_app)
        button_quit.pack(pady=10)

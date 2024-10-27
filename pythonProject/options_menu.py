import tkinter as tk
from tkinter import PhotoImage
from settings import Settings


class OptionsMenu(tk.Frame):
    def __init__(self, master, screen_manager):
        super().__init__(master)
        self.screen_manager = screen_manager

        self.logo_image = PhotoImage(file="logo.png")  # Replace with actual logo path
        logo_label = tk.Label(self, image=self.logo_image)
        logo_label.pack(pady=20)

        self.settings = Settings()

        container = tk.Frame(self)
        container.pack(pady=20, padx=20)

        self.distractor_input = self.create_setting_input(container, "Amount of Distractors:",
                                                          self.settings.get_distractor_amount())
        self.horizontal_cells_input = self.create_setting_input(container, "Amount of Horizontal Cells:",
                                                                self.settings.get_grid_width())
        self.vertical_cells_input = self.create_setting_input(container, "Amount of Vertical Cells:",
                                                              self.settings.get_grid_height())
        self.rounds_input = self.create_setting_input(container, "Amount of Rounds:",
                                                      self.settings.get_number_of_rounds())
        self.seed_input = self.create_setting_input(container, "Current Seed:", self.settings.get_default_seed())

        # Create text boxes for colors
        self.distractor_colour_input = self.create_setting_input(container, "Distractor Colour:",
                                                                 self.settings.get_distractor_colour())
        self.target_colour_input = self.create_setting_input(container, "Target Colour:",
                                                             self.settings.get_target_colour())

        self.default_seed_var = tk.BooleanVar(value=self.settings.get_use_default_seed())
        self.default_seed_checkbox = tk.Checkbutton(
            container, text="Always use default seed", variable=self.default_seed_var, font=("Helvetica", 14)
        )
        self.default_seed_checkbox.pack(anchor="w", pady=5)

        self.skip_eye_test_var = tk.BooleanVar(value=self.settings.get_skip_eye_test())
        self.skip_eye_test_checkbox = tk.Checkbutton(
            container, text="Skip eye test", variable=self.skip_eye_test_var, font=("Helvetica", 14)
        )
        self.skip_eye_test_checkbox.pack(anchor="w", pady=5)

        # Add save and back buttons at the bottom
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        save_button = tk.Button(button_frame, text="Save", command=self.save_settings)
        save_button.pack(side="left", padx=5)

        back_button = tk.Button(button_frame, text="Back", command=lambda: self.screen_manager.show_screen("MainMenu"))
        back_button.pack(side="left", padx=5)

        # Center the entire OptionsMenu
        self.place(relx=0.5, rely=0.5, anchor="center")

    def create_setting_input(self, container, label_text, default_value):
        frame = tk.Frame(container)
        frame.pack(fill="x", pady=5)

        label = tk.Label(frame, text=label_text, font=("Helvetica", 14))
        label.pack(side="left", padx=10)

        input_box = tk.Entry(frame, font=("Helvetica", 14), justify="center")
        input_box.insert(0, str(default_value))  # Set default value
        input_box.pack(side="right", padx=10)

        return input_box

    def save_settings(self):
        """Save the settings when the Save button is clicked."""
        # Retrieve values from each input box and checkboxes, then update the settings
        new_distractor_amount = int(self.distractor_input.get())
        new_horizontal_cells = int(self.horizontal_cells_input.get())
        new_vertical_cells = int(self.vertical_cells_input.get())
        new_rounds = int(self.rounds_input.get())
        new_seed = int(self.seed_input.get())
        new_distractor_colour = self.distractor_colour_input.get()
        new_target_colour = self.target_colour_input.get()

        # Checkbox values
        always_use_default_seed = self.default_seed_var.get()
        skip_eye_test = self.skip_eye_test_var.get()

        # Update settings in the Settings instance
        self.settings.set_distractor_amount(new_distractor_amount)
        self.settings.set_grid_width(new_horizontal_cells)
        self.settings.set_grid_height(new_vertical_cells)
        self.settings.set_number_of_rounds(new_rounds)
        self.settings.set_default_seed(new_seed)
        self.settings.set_distractor_colour(new_distractor_colour)
        self.settings.set_target_colour(new_target_colour)
        self.settings.set_always_use_default_seed(always_use_default_seed)
        self.settings.set_skip_eye_test(skip_eye_test)

        self.settings.save_settings()

        print("Settings saved successfully")

    def start(self):
        """Start method for the settings menu, if needed."""
        print("OptionsMenu displayed.")
class menu_manager:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Manager with Centered Menu")
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", self.exit_app)
        self.screens = {}

        # Add weight to allow window to expand
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

    def add_screen(self, screen_name, screen_frame):
        # Add a new screen to the manager and make it fill the window
        self.screens[screen_name] = screen_frame
        screen_frame.grid(row=0, column=0, sticky="nsew")

    def show_screen(self, screen_name):
        # Bring the selected screen to the front.
        screen = self.screens.get(screen_name)
        if screen:
            screen.tkraise()
            screen.start()

    def exit_app(self, event=None):
        # Exit the application.
        self.root.quit()
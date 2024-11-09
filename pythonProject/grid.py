import random
import tkinter as tk
import time
from score_tracker import ScoreTracker
from circle import Circle
from settings import Settings
import settings

# Menu screen to perform the main experiment
class GridScreen(tk.Frame):
    def __init__(self, master, screen_manager):
        super().__init__(master)
        self.canvas = None
        self.current_seed = None
        self.score_tracker = None
        self.total_rounds = None
        self.current_round = 0
        self.distractor_amount = None
        self.grid_height = None
        self.grid_width = None
        self.finished_all_rounds = False
        self.start_time = None
        self.target_grid = []
        self.screen_manager = screen_manager
        self.should_draw = False
        self.target_colour = "red"
        self.distractor_colour = "blue"
        self.load_settings()
        self.canvas = tk.Canvas(self, width=self.grid_width * 100, height=self.grid_height * 100)
        self.canvas.pack(fill=tk.BOTH, expand=True)

            
    def start(self):
        # start the experiment by resetting and initiating the first round
        self.load_settings()
        self.should_draw = True
        self.current_round = 0
        self.generate_grid()
        self.new_round()
        self.update()
        
    def load_settings(self):
        # Load latest settings from ini file (this is done every first round to ensure the settings are up to date)
        settings = Settings()
        settings.load_settings()
        self.grid_width = settings.get_grid_width()
        self.grid_height = settings.get_grid_height()
        self.distractor_amount = settings.get_distractor_amount()
        self.total_rounds = settings.get_number_of_rounds()
        self.current_round = 0
        self.score_tracker = ScoreTracker(self.current_seed)
        self.current_seed = settings.get_default_seed()

        if not settings.COLOUR_BLIND_MODE:

        self.target_colour = settings.get_target_colour()
        self.distractor_colour = settings.get_distractor_colour()

        # if a seed has been provided then use it, else generate a random one based off of the current time
        if self.current_seed is not None and settings.get_always_use_default_seed():
            random.seed(self.current_seed)
        else:
            self.current_seed = int(time.time() * 1000)
        

    def generate_grid(self):
        # create a grid in a two-dimensional array using the specified width and height
        self.target_grid = [[Circle(j, i, self.target_colour, self.distractor_colour) for j in range(self.grid_width)] for i in range(self.grid_height)]

    def reset_all_targets(self):
        # reset the state of all targets in the grid, setting if distractor and if target to false
        for row in self.target_grid:
            for target in row:
                target.reset()

    def end_all_rounds(self):
        # save scores to csv file, reset targets, ensure the window
        # won't update in the background and then switch back to the main menu screen
        self.score_tracker.export_scores_csv()
        self.finished_all_rounds = True
        self.reset_all_targets()
        self.should_draw = False
        self.screen_manager.show_screen("MainMenu")

    def new_round(self):
        # if last round then stop here and end process
        if self.current_round == self.total_rounds:
            self.end_all_rounds()
            return

        # increase current round
        self.current_round += 1
        self.reset_all_targets()
        self.start_time = time.time()

        #select a sample of distractors from the grid
        flat_grid = [item for sublist in self.target_grid for item in sublist]
        selected_items = random.sample(flat_grid, self.distractor_amount + 1)

        # select a single target from the grid
        target_item = random.choice(selected_items)

        # activate distractor and targets
        for item in selected_items:
            if item != target_item:
                item.set_as_distractor()
            else:
                item.set_as_target()

        # Draw the grid after setting targets
        self.draw()

    def draw(self):
        # Draw the targets on the canvas, scaling to the window size while maintaining aspect ratio
        self.canvas.delete("all")  # Clear the canvas

        # Get the current window size
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # calculate aspect ratio
        grid_aspect_ratio = self.grid_width / self.grid_height

        # Calculate cell size and offsets to maintain aspect ratio
        if canvas_width / canvas_height > grid_aspect_ratio:
            cell_size = canvas_height / self.grid_height
            offset_x = (canvas_width - cell_size * self.grid_width) / 2
            offset_y = 0
        else:
            cell_size = canvas_width / self.grid_width
            offset_y = (canvas_height - cell_size * self.grid_height) / 2
            offset_x = 0

        # Draw each target based on its type (distractor / target)
        for row in self.target_grid:
            for target in row:
                if target.enabled():
                    x1 = target.x * cell_size + offset_x
                    y1 = target.y * cell_size + offset_y
                    x2 = x1 + cell_size
                    y2 = y1 + cell_size

                    # Draw the target or distractor
                    oval_id = self.canvas.create_oval(x1, y1, x2, y2, fill=target.get_colour())

                    # Bind click events based on target type
                    if target.target:
                        self.canvas.tag_bind(oval_id, "<Button-1>", lambda event, t=target: self.on_target_click(event, t))
                    else:
                        self.canvas.tag_bind(oval_id, "<Button-1>", lambda event, t=target: self.on_incorrect_click(event, t))

    def on_target_click(self, event, target):
        # if a target is clicked, increase clicks by one, save scores and start a new round
        print(f"Target at ({target.x}, {target.y}) clicked!")
        elapsed_time = time.time() - self.start_time
        self.score_tracker.increase_clicks()
        self.score_tracker.save_score(elapsed_time)
        self.new_round()

    def on_incorrect_click(self, event, target):
        # if a distractor is clicked, increase the current clicks by one
        print(f"Incorrect target at ({target.x}, {target.y}) clicked!")
        self.score_tracker.increase_clicks()

    def on_resize(self, event):
        # trigger draw() if the screen is resized
        self.draw()

    

    def update(self):
        # continuously update canvas every 500 milliseconds
        self.draw()
        self.after(500, self.update)
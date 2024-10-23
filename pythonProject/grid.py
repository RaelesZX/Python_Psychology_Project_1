import random
import tkinter as tk
import time
from score_tracker import ScoreTracker
from target import Target

class Grid:
    def __init__(self, width,
                 height,
                 distractor_amount,
                 total_rounds,
                 seed_value=None):
        self.start_time = None
        self.grid_width = width
        self.grid_height = height
        self.target_grid = []
        self.distractor_amount = distractor_amount
        self.total_rounds = total_rounds
        self.current_round = 0
        self.score_tracker = ScoreTracker()
        self.finished_all_rounds = False

        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.canvas = tk.Canvas(self.root, width=width * 100, height=height * 100)
        self.canvas.pack(fill=tk.BOTH, expand=True)  # Allow the canvas to expand with window resize
        self.root.bind("<Configure>", self.on_resize)  # Bind window resize event

        self.current_seed = seed_value

        #either used a premade seed or generate a current seed based on current time in miliseconds
        if seed_value is not None:
            random.seed(self.current_seed)
        else:
            current_seed = (time.time() * 1000)

        self.generate_grid()  # Ensure the grid is generated before any drawing happens

    def generate_grid(self):
        """Create the target grid."""
        self.target_grid = [[Target(j, i) for j in range(self.grid_width)] for i in range(self.grid_height)]

    def reset_all_targets(self):
        """Reset the state of all targets."""
        for row in self.target_grid:
            for target in row:
                target.reset()

    def end_all_rounds(self):
        """End all rounds and export the score."""
        self.score_tracker.export_scores_csv()
        self.finished_all_rounds = True
        self.reset_all_targets()

    def new_round(self):
        """Start a new round, reset all targets, and set new target/distractors."""
        if self.current_round == self.total_rounds:
            self.end_all_rounds()
            return

        self.current_round += 1

        self.reset_all_targets()
        self.start_time = time.time()

        flat_grid = [item for sublist in self.target_grid for item in sublist]
        selected_items = random.sample(flat_grid, self.distractor_amount + 1)
        target_item = random.choice(selected_items)

        for item in selected_items:
            if item != target_item:
                item.set_as_distractor()
            else:
                item.set_as_target()

    def draw(self):
        """Draw the targets on the canvas, scaling to the window size while maintaining aspect ratio."""
        self.canvas.delete("all")  # Clear the canvas

        # Get the current window size
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # Calculate the aspect ratio of the grid
        grid_aspect_ratio = self.grid_width / self.grid_height

        # Find the limiting dimension to maintain aspect ratio
        if canvas_width / canvas_height > grid_aspect_ratio:
            # Height is the limiting factor, so scale based on height
            cell_size = canvas_height / self.grid_height
            offset_x = (canvas_width - cell_size * self.grid_width) / 2  # Center horizontally
            offset_y = 0
        else:
            # Width is the limiting factor, so scale based on width
            cell_size = canvas_width / self.grid_width
            offset_y = (canvas_height - cell_size * self.grid_height) / 2  # Center vertically
            offset_x = 0

        for row in self.target_grid:
            for target in row:
                if target.enabled():
                    # Scale the position and size based on the window size, maintaining aspect ratio
                    x1 = target.x * cell_size + offset_x
                    y1 = target.y * cell_size + offset_y
                    x2 = x1 + cell_size
                    y2 = y1 + cell_size

                    # Draw oval (circle)
                    oval_id = self.canvas.create_oval(x1, y1, x2, y2, fill=target.get_colour())

                    # Bind click events based on the type of target
                    if target.target:
                        self.canvas.tag_bind(oval_id, "<Button-1>", lambda event, t=target: self.on_target_click(event, t))
                    else:
                        self.canvas.tag_bind(oval_id, "<Button-1>", lambda event, t=target: self.on_incorrect_click(event, t))

    def on_target_click(self, event, target):
        """Handle correct target click."""
        print(f"Target at ({target.x}, {target.y}) clicked!")
        elapsed_time = time.time() - self.start_time
        self.score_tracker.increase_clicks()
        self.score_tracker.save_score(elapsed_time)
        self.new_round()

    def on_incorrect_click(self, event, target):
        """Handle incorrect target click."""
        print(f"Target at ({target.x}, {target.y}) incorrectly clicked!")
        self.score_tracker.increase_clicks()

    def on_resize(self, event):
        """Redraw targets when window is resized."""
        self.draw()  # Redraw the targets to fit the new window size

    def update(self):
        """Continuously update the canvas."""
        self.draw()  # Ensure the targets are drawn
        self.root.after(500, self.update)  # Schedule the update method to be called every 500ms (0.5 seconds)

    def run(self):
        """Run the Tkinter loop."""
        self.update()  # Start the update loop
        self.root.mainloop()

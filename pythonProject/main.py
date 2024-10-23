from grid import Grid
from settings import Settings

# Load settings
settings = Settings()
amount_of_distractors = settings.get_distractor_amount()
amount_of_horizontal_cells = settings.get_grid_width()
amount_of_vertical_cells = settings.get_grid_height()
amount_of_rounds = settings.get_number_of_rounds()
current_seed = settings.get_default_seed()

grid = Grid(amount_of_horizontal_cells,
            amount_of_vertical_cells,
            amount_of_distractors,
            amount_of_rounds,
            current_seed)

grid.generate_grid()
grid.new_round()

if __name__ == "__main__":
    if not grid.finished_all_rounds:
        grid.run()
    else:
        exit()

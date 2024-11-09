import configparser
import os

class Settings:
    COLOUR_BLIND_MODE = False
    def __init__(self):
        self.current_settings = None
        self.name_of_file = 'settings.ini'
        self.create_default_settings_file()
        self.load_settings()

    def get_default_settings(self):
        # The default format of the ini files which is used if no ini file exists
        return {
            'grid': {
                'height': '10',
                'width': '10',
                'distractors': '4',
                'number_of_rounds': '5',
                'target_colour': 'red',
                'distractor_colour': 'blue'
            },
            'general': {
                'default_seed': '12345',
                'use_default_seed': 'True',
                'skip_eye_test': 'False',
                'save_file_name': 'experiment_output_1'
            }
        }

    def create_default_settings_file(self):
        # check if ini file exists, if it doesn't then create the file and write in the default settings
        if not os.path.isfile(self.name_of_file):
            self.current_settings = configparser.ConfigParser()
            self.current_settings.read_dict(self.get_default_settings())
            with open(self.name_of_file, 'w') as configfile:
                self.current_settings.write(configfile)
            print(f"Default settings file created: {self.name_of_file}")

    def save_settings(self):
        # override the current ini file with the new settings
        with open(self.name_of_file, 'w') as configfile:
            self.current_settings.write(configfile)
        print("Settings saved to file.")

    def load_settings(self):
        # Load settings from the file or use default settings
        self.current_settings = configparser.ConfigParser()
        if os.path.exists(self.name_of_file):
            self.current_settings.read(self.name_of_file)
        else:
            self.current_settings.read_dict(self.get_default_settings())
            print("Settings file not found. Using default settings.")

    # Accessor methods to retrieve specific settings
    def get_grid_width(self):
        return self.current_settings.getint('grid', 'width')

    def get_grid_height(self):
        return self.current_settings.getint('grid', 'height')

    def get_distractor_amount(self):
        return self.current_settings.getint('grid', 'distractors')

    def get_number_of_rounds(self):
        return self.current_settings.getint('grid', 'number_of_rounds')

    def get_default_seed(self):
        return self.current_settings.getint('general', 'default_seed')

    def get_target_colour(self):
        return self.current_settings.get('grid', 'target_colour')

    def get_distractor_colour(self):
        return self.current_settings.get('grid', 'distractor_colour')

    def get_always_use_default_seed(self):
        return self.current_settings.getboolean('general', 'use_default_seed')

    def get_skip_eye_test(self):
        return self.current_settings.getboolean('general', 'skip_eye_test')

    def get_save_file_name(self):
        return self.current_settings.get('general', 'save_file_name') + ".csv"

    # Methods to set specific settings
    def set_distractor_amount(self, new_distractor_amount):
        self.current_settings.set('grid', 'distractors', str(new_distractor_amount))
        self.save_settings()

    def set_grid_width(self, new_horizontal_cells):
        self.current_settings.set('grid', 'width', str(new_horizontal_cells))
        self.save_settings()

    def set_grid_height(self, new_vertical_cells):
        self.current_settings.set('grid', 'height', str(new_vertical_cells))
        self.save_settings()

    def set_number_of_rounds(self, new_rounds):
        self.current_settings.set('grid', 'number_of_rounds', str(new_rounds))
        self.save_settings()

    def set_default_seed(self, new_seed):
        self.current_settings.set('general', 'default_seed', str(new_seed))
        self.save_settings()

    def set_distractor_colour(self, new_distractor_colour):
        self.current_settings.set('grid', 'distractor_colour', new_distractor_colour)
        self.save_settings()

    def set_target_colour(self, new_target_colour):
        self.current_settings.set('grid', 'target_colour', new_target_colour)
        self.save_settings()

    def set_always_use_default_seed(self, always_use_default_seed):
        self.current_settings.set('general', 'use_default_seed', str(always_use_default_seed))
        self.save_settings()

    def set_skip_eye_test(self, skip_eye_test):
        self.current_settings.set('general', 'skip_eye_test', str(skip_eye_test))
        self.save_settings()

    def set_save_file_name(self, save_file_name):
        self.current_settings.set('general', 'save_file_name', save_file_name)

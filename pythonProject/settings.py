import configparser
import os

class Settings:
    def __init__(self):
        self.current_settings = None
        self.name_of_file = 'settings.ini'
        self.create_default_settings_file()
        self.load_settings()

    def get_default_settings(self):
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
            }
        }

    def create_default_settings_file(self):
        """Create a default settings file if it doesn't exist."""
        if not os.path.isfile(self.name_of_file):
            self.current_settings = configparser.ConfigParser()
            self.current_settings.read_dict(self.get_default_settings())
            with open(self.name_of_file, 'w') as configfile:
                self.current_settings.write(configfile)
            print(f"Default settings file created: {self.name_of_file}")

    def load_settings(self):
        """Load settings from the file or use default settings."""
        self.current_settings = configparser.ConfigParser()
        if os.path.exists(self.name_of_file):
            self.current_settings.read(self.name_of_file)
        else:
            self.current_settings.read_dict(self.get_default_settings())
            print(f"Settings file not found. Using default settings.")

    # Accessor methods to retrieve specific settings
    def get_grid_width(self):
        return self.current_settings.getint('grid', 'width')

    def get_grid_height(self):
        return self.current_settings.getint('grid', 'height')

    def get_distractor_amount(self):
        return self.current_settings.getint('grid', 'distractors')

    def get_number_of_rounds(self):
        return self.current_settings.getint('grid', 'number_of_rounds')  # Changed from 'general' to 'grid'

    def get_default_seed(self):
        return self.current_settings.getint('general', 'default_seed')

    def get_target_colour(self):
        return self.current_settings.get('general', 'target_colour')

    def get_distractor_colour(self):
        return self.current_settings.get('general', 'distractor_colour')

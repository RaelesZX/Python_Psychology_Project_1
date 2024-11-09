from collections import namedtuple
import csv
import os
import uuid

from pythonProject.settings import Settings

Score = namedtuple('Score', ['Time', 'Clicks'])

class ScoreTracker:

    def __init__(self, seed):
        self.scores = []
        self.clicks = 0
        self.seed = seed
        settings = Settings()
        settings.load_settings()
        self.save_file_name = settings.get_save_file_name()

    def increase_clicks(self):
        # clicks will only ever increase by one at a time
        self.clicks += 1

    def save_score(self, time):
        # score is recorded in the array and clicks is set to 0 ready for the next round
        self.scores.append(Score(time, self.clicks))
        self.clicks = 0

    def export_scores_csv(self):
        # choose to append or create file
        mode = 'a' if os.path.exists(self.save_file_name) else 'w'

        # scores are saved to a csv file
        with open(self.save_file_name, mode, newline='') as file:
            writer = csv.writer(file)

            if mode == 'w':
                writer.writerow(['User ID', 'Time', 'Clicks', 'Seed'])

            user_id = str(uuid.uuid4())  # Generate a GUID as a string - always unique

            for score in self.scores:
                writer.writerow([user_id, score.Time, score.Clicks, self.seed])

    def reset(self):
        # reset score arrays for a new experiment
        self.scores = []

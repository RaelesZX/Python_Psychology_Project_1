from collections import namedtuple
import csv

Score = namedtuple('Score', ['Time', 'Clicks'])

class ScoreTracker:

    def __init__(self):
        self.scores = []
        self.clicks = 0

    def increase_clicks(self):
        self.clicks += 1

    def save_score(self, time):
        self.scores.append(Score(time, self.clicks))
        self.clicks = 0

    def export_scores_csv(self):
        with open('scores.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Time', 'Clicks'])

            for score in self.scores:
                writer.writerow([score.Time, score.Clicks])

    def reset(self):
        self.scores = []

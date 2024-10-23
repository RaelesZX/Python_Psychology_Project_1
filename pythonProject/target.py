# target.py
class Target:
    def __init__(self, x, y):
        self.distractor = False
        self.target = False
        self.clicked = False
        self.x = x
        self.y = y

    def set_as_target(self):
        self.distractor = False
        self.target = True

    def set_as_distractor(self):
        self.distractor = True
        self.target = False

    def enabled(self):
        if self.distractor or self.target:
            return True
        else:
            return False

    def get_colour(self):
        if self.distractor:
            return "blue"
        else:
            return "red"

    def reset(self):
        self.distractor = False
        self.target = False

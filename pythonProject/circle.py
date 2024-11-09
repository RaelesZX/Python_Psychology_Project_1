# target.py
class Circle:
    def __init__(self, x, y, target_colour, distractor_colour):
        self.distractor = False
        self.target = False
        self.x = x
        self.y = y
        self.target_colour = target_colour
        self.distractor_colour = distractor_colour

    def set_as_target(self):
        # sets as target to true and distractor as false. It cannot be both at the same time
        self.distractor = False
        self.target = True

    def set_as_distractor(self):
        # sets as target to false and distractor as true. It cannot be both at the same time
        self.distractor = True
        self.target = False

    def enabled(self):
        # considered to be enabled if it's either a target or distractor, or else it's inactive and of no use
        if self.distractor or self.target:
            return True
        else:
            return False

    def get_colour(self):
        # blue if distractor, red if target
        if self.distractor:
            return self.distractor_colour
        else:
            return self.target_colour

    def reset(self):
        # deactivate
        self.distractor = False
        self.target = False

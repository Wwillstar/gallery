from random import randint


class Die():
    """represent a die"""

    def __init__(self, num_sides=6):
        """die has six sides"""
        self.num_sides = num_sides

    def roll(self):
        """ return a random number ranged between 1 and num_size """
        return randint(1, self.num_sides)

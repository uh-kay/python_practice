from random import randint

class Die:
    """An attempt to model a die."""

    def __init__(self, sides=6):
        """Initializes die attributes."""
        self.sides = sides

    def roll_die(self):
        """Rolls a random number according to the number of sides."""
        die_roll = randint(1, self.sides)
        print(die_roll)

import random
class Powerup:
    def __init__(self, pos, type):
        self.type = type
        self.position = pos

powerup_proportion = 0.8

def random_powerup(pos):
    return Powerup(pos, random.randrange(3))

import random


class AtomBlue():
    max_atoms_number = 50
    radius = 1
    max_v = 10
    mass = 1

    def __init__(self):
        self.v_x, self.v_y = random.randint(-self.max_v, self.max_v), random.randint(-self.max_v, self.max_v)

        # self.x =
        # self.y =

# class AtomRed():

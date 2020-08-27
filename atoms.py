import random
import math
import settings


def add_atoms(N):
    AtomRed()
    for i in range(N):
        AtomBlue()


class AtomBlue:
    atoms_list = []

    def __init__(self):
        self.v_x, self.v_y = random.randint(-settings.max_v, settings.max_v), random.randint(-settings.max_v,
                                                                                             settings.max_v)
        while True:
            test = True
            x = random.randint(0 + settings.radius, settings.width - settings.radius)
            y = random.randint(0 + settings.radius, settings.height - settings.radius)
            for i in range(len(AtomBlue.atoms_list)):
                if math.sqrt((AtomBlue.atoms_list[i].x - x) ** 2 + (
                        AtomBlue.atoms_list[i].y - y) ** 2) <= 2 * settings.radius:
                    test = False
            if test:
                self.x = x
                self.y = y
                break
        AtomBlue.atoms_list.append(self)

        
class AtomRed:

    def __init__(self):
        self.v_x, self.v_y = random.randint(0, settings.max_v), random.randint(0, settings.max_v)
        self.x = settings.radius
        self.y = settings.radius
        AtomBlue.atoms_list.append(self)
        self.collisions = 1
        self.path = 0

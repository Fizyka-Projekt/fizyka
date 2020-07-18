import random
import math
import settings

class AtomBlue:
    max_atoms_number = 50
    radius = 1
    max_v = 10
    mass = 1
    atoms_list = []

    def __init__(self):
        self.v_x, self.v_y = random.randint(-self.max_v, self.max_v), random.randint(-self.max_v, self.max_v)
        while True:
            test = True
            x = random.randint(0 + AtomBlue.radius, settings.length - AtomBlue.radius)
            y = random.randint(0 + AtomBlue.radius, settings.height - AtomBlue.radius)
            for i in range(len(AtomBlue.atoms_list)):
                if math.sqrt((AtomBlue.atoms_list[i].x - x) ** 2 + (
                        AtomBlue.atoms_list[i].y - y) ** 2) < 2 * AtomBlue.radius:
                    test = False
            if test:
                self.x = x
                self.y = y
                break
        AtomBlue.atoms_list.append(self)

import random
import math
import settings


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

    def move(self):
        self.x = self.x + self.v_x * settings.dt
        self.y = self.y + self.v_y * settings.dt



    def collision(self, enemy):

        enemy_id = AtomBlue.atoms_list.index(enemy)

        atom_list[j].x = atom_list[j].x + atom_list[j].v_x * settings.dt
        atom_list[j].y = atom_list[j].y + atom_list[j].v_y * settings.dt
        
class AtomRed:

    def __init__(self):
        self.v_x, self.v_y = random.randint(0, settings.max_v), random.randint(0, settings.max_v)
        self.x = settings.radius
        self.y = settings.radius
        AtomBlue.atoms_list.append(self)

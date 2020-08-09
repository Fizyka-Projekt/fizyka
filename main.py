import atoms
import settings
import animation
import math
import numpy as np


atom_list = atoms.AtomBlue.atoms_list

atoms.AtomRed()
for i in range(settings.atoms_number):
    atoms.AtomBlue()



animation.draw()


def change_position(i):
    if settings.radius + settings.d > atom_list[i].x > atom_list[i].x + atom_list[i].v_x * settings.dt or atom_list[
        i].x > settings.width - settings.radius - settings.d and atom_list[i].x + atom_list[i].v_x * settings.dt > \
            atom_list[i].x:
        atom_list[i].v_x = -atom_list[i].v_x
    if settings.radius + settings.d > atom_list[i].y > atom_list[i].y + atom_list[i].v_y * settings.dt or atom_list[
        i].y > settings.height - settings.radius - settings.d and atom_list[i].y + atom_list[i].v_y * settings.dt > \
            atom_list[i].y:
        atom_list[i].v_y = -atom_list[i].v_y

    atom_list[i].x = atom_list[i].x + atom_list[i].v_x * settings.dt
    atom_list[i].y = atom_list[i].y + atom_list[i].v_y * settings.dt


def change_v(i):
    test = True
    def change_velocities(j,k):
        r_1 = np.array((atom_list[j].x, atom_list[j].y))
        r_2 = np.array((atom_list[k].x, atom_list[k].y))
        v_1 = np.array((atom_list[j].v_x, atom_list[j].v_y))
        v_2 = np.array((atom_list[k].v_x, atom_list[k].v_y))
        d = np.linalg.norm(r_1 - r_2) ** 2
        u_1 = v_1 - np.dot(v_1 - v_2, r_1 - r_2) / d * (r_1 - r_2)
        u_2 = v_2 - np.dot(v_2 - v_1, r_2 - r_1) / d * (r_2 - r_1)
        atom_list[j].v_x = u_1[0]
        atom_list[j].v_y = u_1[1]
        atom_list[k].v_x = u_2[0]
        atom_list[k].v_y = u_2[1]


    for j in range(i+1,settings.atoms_number+1):
        d = math.sqrt((atom_list[i].x - atom_list[j].x) ** 2 + (atom_list[i].y - atom_list[j].y) ** 2)
        next_1_x = atom_list[i].x + atom_list[i].v_x * settings.dt
        next_1_y = atom_list[i].y + atom_list[i].v_y * settings.dt
        next_2_x = atom_list[j].x + atom_list[j].v_x * settings.dt
        next_2_y = atom_list[j].y + atom_list[j].v_y * settings.dt
        d_after = math.sqrt((next_1_x - next_2_x) ** 2 + (next_1_y - next_2_y) ** 2)
        if d <= 2 * settings.radius + settings.d and d_after < d:
            change_velocities(i, j)
            test = False
    return test


while True:
    for i in range(settings.atoms_number+1):
        test = change_v(i)
        if test:
            change_position(i)
    animation.draw()

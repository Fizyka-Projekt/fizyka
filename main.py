import sys
import atoms
import settings
import animation
import time
import math


# standard value settings:
# atoms.AtomBlue.max_v = 10
# atoms.radius = 1
# atoms.mass = 1

# print Class info
# print(AtomBlue.__dict__)settings.max_atoms_number

# # eg. list of atoms
# atoms = list(AtomBlue() for x in range(5))
#
# for a in atoms:
#     print(a.__dict__)
#     print("V:", a.v_x, a.v_y)

print("Wysokosc:", settings.height, "\nSzerokosc:", settings.width)

for i in range(20):
    atoms.AtomBlue()

for i in range(20):
    print("x:",     atoms.AtomBlue.atoms_list[i].x,
          "y:",     atoms.AtomBlue.atoms_list[i].y,
          "v_x:",   atoms.AtomBlue.atoms_list[i].v_x,
          "v_y:",   atoms.AtomBlue.atoms_list[i].v_y)

animation.draw()

for i in range(1000):
    for j in range(20):
        for k in range(20):
            if 2 * settings.radius < (math.sqrt(
                    (atoms.AtomBlue.atoms_list[k].x - atoms.AtomBlue.atoms_list[j].x) ** 2 + (
                            atoms.AtomBlue.atoms_list[k].y - atoms.AtomBlue.atoms_list[
                        j].y) ** 2)) <= 2 * settings.radius + settings.d:
                normal_x = (atoms.AtomBlue.atoms_list[k].x - atoms.AtomBlue.atoms_list[j].x) / (math.sqrt(
                    (atoms.AtomBlue.atoms_list[k].x - atoms.AtomBlue.atoms_list[j].x) ** 2 + (
                            atoms.AtomBlue.atoms_list[k].y - atoms.AtomBlue.atoms_list[j].y) ** 2))
                normal_y = (atoms.AtomBlue.atoms_list[k].y - atoms.AtomBlue.atoms_list[j].y) / (math.sqrt(
                    (atoms.AtomBlue.atoms_list[k].x - atoms.AtomBlue.atoms_list[j].x) ** 2 + (
                            atoms.AtomBlue.atoms_list[k].y - atoms.AtomBlue.atoms_list[j].y) ** 2))
                tangential_x = (-(atoms.AtomBlue.atoms_list[k].y - atoms.AtomBlue.atoms_list[j].y)) / (math.sqrt(
                    (atoms.AtomBlue.atoms_list[k].x - atoms.AtomBlue.atoms_list[j].x) ** 2 + (
                            atoms.AtomBlue.atoms_list[k].y - atoms.AtomBlue.atoms_list[j].y) ** 2))
                tangential_y = normal_x
                velo_norm_1_x = atoms.AtomBlue.atoms_list[j].v_x * normal_x
                velo_norm_1_y = atoms.AtomBlue.atoms_list[j].v_y * normal_y
                velo_tange_1_x = atoms.AtomBlue.atoms_list[j].v_x * tangential_x
                velo_tange_1_y = atoms.AtomBlue.atoms_list[j].v_y * tangential_y
                velo_norm_2_x = atoms.AtomBlue.atoms_list[k].v_x * normal_x
                velo_norm_2_y = atoms.AtomBlue.atoms_list[k].v_y * normal_y
                velo_tange_2_x = atoms.AtomBlue.atoms_list[k].v_x * tangential_x
                velo_tange_2_y = atoms.AtomBlue.atoms_list[k].v_y * tangential_y
                velo_norm_1_p_x = velo_norm_2_x
                velo_norm_1_p_y = velo_norm_2_y
                velo_norm_2_p_x = velo_norm_1_x
                velo_norm_2_p_y = velo_norm_1_y
                v_1_prim_x = velo_norm_1_p_x * normal_x + velo_tange_1_x * tangential_x
                v_1_prim_y = velo_norm_1_p_y * normal_y + velo_tange_1_y * tangential_y
                v_2_prim_x = velo_norm_2_p_x * normal_x + velo_tange_2_x * tangential_x
                v_2_prim_y = velo_norm_2_p_y * normal_y + velo_tange_2_y * tangential_y
                atoms.AtomBlue.atoms_list[j].v_x = int(v_1_prim_x)
                atoms.AtomBlue.atoms_list[j].v_y = int(v_1_prim_y)
                atoms.AtomBlue.atoms_list[k].v_x = int(v_2_prim_x)
                atoms.AtomBlue.atoms_list[k].v_y = int(v_2_prim_y)
        if atoms.AtomBlue.atoms_list[j].x < settings.radius + settings.d or atoms.AtomBlue.atoms_list[j].x > settings.width - settings.radius - settings.d:
            atoms.AtomBlue.atoms_list[j].v_x = -atoms.AtomBlue.atoms_list[j].v_x
        if atoms.AtomBlue.atoms_list[j].y < settings.radius + settings.d or atoms.AtomBlue.atoms_list[j].y > settings.height - settings.radius - settings.d:
            atoms.AtomBlue.atoms_list[j].v_y = -atoms.AtomBlue.atoms_list[j].v_y
            
        atoms.AtomBlue.atoms_list[j].x = atoms.AtomBlue.atoms_list[j].x + atoms.AtomBlue.atoms_list[j].v_x * settings.dt
        atoms.AtomBlue.atoms_list[j].y = atoms.AtomBlue.atoms_list[j].y + atoms.AtomBlue.atoms_list[j].v_y * settings.dt
    animation.draw()

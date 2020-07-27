import sys
import atoms
import settings
import animation
import time
import math

atom_list = atoms.AtomBlue.atoms_list
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

for i in range(20):
    atoms.AtomBlue()

# for i in range(20):
#     print("x:", atom_list[i].x,
#           "y:", atom_list[i].y,
#           "v_x:", atom_list[i].v_x,
#           "v_y:", atom_list[i].v_y)

animation.draw()

for i in range(settings.M):
    for j in range(20):
        for k in range(20):
            if 2 * settings.radius < (math.sqrt(
                    (atom_list[k].x - atom_list[j].x) ** 2 + (
                            atom_list[k].y - atom_list[
                        j].y) ** 2)) <= 2 * settings.radius + settings.d:
                normal_x = (atom_list[k].x - atom_list[j].x) / (math.sqrt(
                    (atom_list[k].x - atom_list[j].x) ** 2 + (
                            atom_list[k].y - atom_list[j].y) ** 2))
                normal_y = (atom_list[k].y - atom_list[j].y) / (math.sqrt(
                    (atom_list[k].x - atom_list[j].x) ** 2 + (
                            atom_list[k].y - atom_list[j].y) ** 2))
                tangential_x = (-(atom_list[k].y - atom_list[j].y)) / (math.sqrt(
                    (atom_list[k].x - atom_list[j].x) ** 2 + (
                            atom_list[k].y - atom_list[j].y) ** 2))
                tangential_y = normal_x
                velo_norm_1_x = atom_list[j].v_x * normal_x
                velo_norm_1_y = atom_list[j].v_y * normal_y
                velo_tange_1_x = atom_list[j].v_x * tangential_x
                velo_tange_1_y = atom_list[j].v_y * tangential_y
                velo_norm_2_x = atom_list[k].v_x * normal_x
                velo_norm_2_y = atom_list[k].v_y * normal_y
                velo_tange_2_x = atom_list[k].v_x * tangential_x
                velo_tange_2_y = atom_list[k].v_y * tangential_y
                velo_norm_1_p_x = velo_norm_2_x
                velo_norm_1_p_y = velo_norm_2_y
                velo_norm_2_p_x = velo_norm_1_x
                velo_norm_2_p_y = velo_norm_1_y
                v_1_prim_x = velo_norm_1_p_x * normal_x + velo_tange_1_x * tangential_x
                v_1_prim_y = velo_norm_1_p_y * normal_y + velo_tange_1_y * tangential_y
                v_2_prim_x = velo_norm_2_p_x * normal_x + velo_tange_2_x * tangential_x
                v_2_prim_y = velo_norm_2_p_y * normal_y + velo_tange_2_y * tangential_y
                atom_list[j].v_x = v_1_prim_x
                atom_list[j].v_y = v_1_prim_y
                atom_list[k].v_x = v_2_prim_x
                atom_list[k].v_y = v_2_prim_y
        if atom_list[j].x < settings.radius + settings.d or atom_list[
            j].x > settings.width - settings.radius - settings.d:
            atom_list[j].v_x = -atom_list[j].v_x
        if atom_list[j].y < settings.radius + settings.d or atom_list[
            j].y > settings.height - settings.radius - settings.d:
            atom_list[j].v_y = -atom_list[j].v_y

        atom_list[j].x = atom_list[j].x + atom_list[j].v_x * settings.dt
        atom_list[j].y = atom_list[j].y + atom_list[j].v_y * settings.dt
    animation.draw()
print(settings.dt)

import sys
import atoms
import settings
import animation
import time


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

for i in range(7):
    atoms.AtomBlue()

for i in range(7):
    print("x:",     atoms.AtomBlue.atoms_list[i].x,
          "y:",     atoms.AtomBlue.atoms_list[i].y,
          "v_x:",   atoms.AtomBlue.atoms_list[i].v_x,
          "v_y:",   atoms.AtomBlue.atoms_list[i].v_y)

animation.draw()

for i in range(settings.M):
    for j in range(7):
        atoms.AtomBlue.atoms_list[j].x = atoms.AtomBlue.atoms_list[j].x + atoms.AtomBlue.atoms_list[j].v_x * settings.dt
        atoms.AtomBlue.atoms_list[j].y = atoms.AtomBlue.atoms_list[j].y + atoms.AtomBlue.atoms_list[j].v_y * settings.dt
    animation.draw()

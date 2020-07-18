import sys
import atoms
import box

# standard value settings:
# atoms.AtomBlue.max_v = 10
# atoms.radius = 1
# atoms.mass = 1

# print Class info
# print(AtomBlue.__dict__)

# # eg. list of atoms
# atoms = list(AtomBlue() for x in range(5))
#
# for a in atoms:
#     print(a.__dict__)
#     print("V:", a.v_x, a.v_y)
box.Box()
for i in range(5):
    atoms.AtomBlue()

for i in range(5):
    print("x:", atoms.AtomBlue.atoms_list[i].x, "y:", atoms.AtomBlue.atoms_list[i].y, "v_x:",
          atoms.AtomBlue.atoms_list[i].v_x, "v_y:",
          atoms.AtomBlue.atoms_list[i].v_y)

print("wysokosc", box.Box.boxi.height)

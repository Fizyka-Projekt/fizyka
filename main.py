import atoms


# standard value settings:
atoms.AtomBlue.max_v = 3
atoms.radius = 1
atoms.mass = 1

# print Class info
# print(AtomBlue.__dict__)

for i in range(5):
    atoms.AtomBlue()

for i in range(5):
    print("x:", atoms.AtomBlue.atoms_list[i].x, "y:", atoms.AtomBlue.atoms_list[i].y, "v_x:", atoms.AtomBlue.atoms_list[i].v_x, "v_y:",
          atoms.AtomBlue.atoms_list[i].v_y)
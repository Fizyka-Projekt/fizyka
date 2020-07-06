from atom import AtomBlue


# standard value settings:
AtomBlue.max_v = 10
AtomBlue.radius = 1
AtomBlue.mass = 1

# print Class info
# print(AtomBlue.__dict__)

# # eg. list of atoms
# atoms = list(AtomBlue() for x in range(5))
#
# for a in atoms:
#     print(a.__dict__)
#     print("V:", a.v_x, a.v_y)

for i in range(5):
    AtomBlue()



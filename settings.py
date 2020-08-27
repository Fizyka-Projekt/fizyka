radius = 1
max_v = 10
mass = 1
max_atoms_number = 50  # int(0.25 * min([n_H, n_L]))

n_H = 50
n_L = n_H
height = n_H * radius
width = n_L * radius

atoms_number = 12

k = 4  # min([n_H, n_L])
dt = 1 / (k * max_v)  # time step
frames = 30
Dt = frames * dt  # total time
d = radius / 10  # tolerance
radius_plus = radius + d  # radius with tolerance

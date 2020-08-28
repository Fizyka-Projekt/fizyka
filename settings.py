radius = 1
max_v = 10
mass = 1


n_H = 20
n_L = n_H
height = n_H * radius
width = n_L * radius

max_atoms_number = 50
atoms_number = 12

k = 20
dt = 1 / (k * max_v)  # time step
frames = 250
Dt = frames * dt  # total time
d = radius / 10  # tolerance
radius_plus = radius + d  # radius with tolerance

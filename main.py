import atoms
import settings
import animation
import math
import numpy as np

path = 0
collisions = 0

def add_atoms(N):
    atoms.AtomRed()
    for i in range(N):
        atoms.AtomBlue()


def change_position(i):
    global path
    global collisions
    if settings.radius + settings.d > atom_list[i].x > atom_list[i].x + atom_list[i].v_x * settings.dt or atom_list[
        i].x > settings.width - settings.radius - settings.d and atom_list[i].x + atom_list[i].v_x * settings.dt > \
            atom_list[i].x:
        atom_list[i].v_x = -atom_list[i].v_x
    if settings.radius + settings.d > atom_list[i].y > atom_list[i].y + atom_list[i].v_y * settings.dt or atom_list[
        i].y > settings.height - settings.radius - settings.d and atom_list[i].y + atom_list[i].v_y * settings.dt > \
            atom_list[i].y:
        atom_list[i].v_y = -atom_list[i].v_y

    if i == 0:
        path = path + math.sqrt(atom_list[i].v_x * atom_list[i].v_x + atom_list[i].v_y * atom_list[i].v_y) * settings.dt

    atom_list[i].x = atom_list[i].x + atom_list[i].v_x * settings.dt
    atom_list[i].y = atom_list[i].y + atom_list[i].v_y * settings.dt


def change_v(i,N):

    def change_velocities(j, k):
        r1 = np.array((atom_list[j].x, atom_list[j].y))
        r2 = np.array((atom_list[k].x, atom_list[k].y))
        v1 = np.array((atom_list[j].v_x, atom_list[j].v_y))
        v2 = np.array((atom_list[k].v_x, atom_list[k].v_y))
        d = np.linalg.norm(r1 - r2)
        n = (r2 - r1) / d
        t = np.array((-n[1], n[0]))
        v1n = np.dot(v2, n)
        v2n = np.dot(v1, n)
        v1t = np.dot(v1, t)
        v2t = np.dot(v2, t)
        atom_list[j].v_x = (v1n * (r2[0] - r1[0]) - v1t * (r2[1] - r1[1])) / d
        atom_list[j].v_y = (v1n * (r2[1] - r1[1]) + v1t * (r2[0] - r1[0])) / d
        atom_list[k].v_x = (v2n * (r2[0] - r1[0]) - v2t * (r2[1] - r1[1])) / d
        atom_list[k].v_y = (v2n * (r2[1] - r1[1]) + v2t * (r2[0] - r1[0])) / d

    for j in range(i+1,N+1):
        d = math.sqrt((atom_list[i].x - atom_list[j].x) ** 2 + (atom_list[i].y - atom_list[j].y) ** 2)
        next_1_x = atom_list[i].x + atom_list[i].v_x * settings.dt
        next_1_y = atom_list[i].y + atom_list[i].v_y * settings.dt
        next_2_x = atom_list[j].x + atom_list[j].v_x * settings.dt
        next_2_y = atom_list[j].y + atom_list[j].v_y * settings.dt
        d_after = math.sqrt((next_1_x - next_2_x) ** 2 + (next_1_y - next_2_y) ** 2)
        if 2*settings.radius < d <= 2 * settings.radius + settings.d and d > d_after:
            change_velocities(i, j)
        if d_after < d <= 2*settings.radius:
            change_velocities(i, j)

plot_xdata = [x for x in range(10, settings.max_atoms_number, 5)]
plot_ydata = []
plot2_ydata = []
Mlist = [10, 20, 50, 100]

animation.draw(1)
if settings.atoms_number not in plot_xdata:
    plot_xdata.append(settings.atoms_number)
    plot_xdata.sort()
if settings.frames not in Mlist:
    Mlist.append(settings.frames)
    Mlist.sort()

for M in Mlist:
    for N in plot_xdata:
        path = 0
        collisions = 1
        atoms.AtomBlue.atoms_list = []
        atom_list = atoms.AtomBlue.atoms_list
        add_atoms(N)
        if N == settings.atoms_number and M == settings.frames:
            animation.draw(0)
        for j in range(M):
            for k in range(N + 1):
                change_position(k)
            for i in range(N + 1):
                change_v(i,N)
            if N == settings.atoms_number and M == settings.frames:
                animation.draw(0)
        plot_ydata.append(path/collisions)
        plot2_ydata.append(collisions/M*settings.dt)
        if N == settings.atoms_number and M == settings.frames:
            print("Please wait until all calculations are finished")

animation.plots(plot_xdata,plot_ydata,plot2_ydata,Mlist)

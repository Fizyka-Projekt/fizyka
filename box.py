import atoms


class Box:
    n_H = 10
    n_L = 10
    height = n_H * atom.AtomBlue.radius
    length = n_L * atom.AtomBlue().radius
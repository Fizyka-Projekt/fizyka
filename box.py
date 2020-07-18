import atoms

class Box:
    def __init__(self):
        self.n_H = 10
        self.n_L = 10
        self.height = self.n_H * atoms.AtomBlue.radius
        self.length = self.n_L * atoms.AtomBlue.radius
        Box.boxi = self
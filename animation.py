import matplotlib.pyplot as plt
from atoms import AtomBlue as Atom
import settings


def vis():
    plt.plot([c.x for c in Atom.atoms_list], [c.y for c in Atom.atoms_list], 'ro')
    plt.axis('off')
    plt.show()

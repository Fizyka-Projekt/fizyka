import matplotlib.pyplot as plt
from atoms import AtomBlue as Atom
import settings

def draw():
    plt.scatter([c.x for c in Atom.atoms_list], [c.y for c in Atom.atoms_list], s=100, c='b', marker='o')
    plt.axis([0, settings.width, 0, settings.height])
    plt.draw()
    plt.pause(0.01)
    plt.clf()


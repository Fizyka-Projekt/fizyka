import matplotlib.pyplot as plt
import matplotlib
from atoms import AtomBlue as Atom
import settings


def draw():
    plt.axes(xlim=(0, settings.width), ylim=(0, settings.height))
    plt.scatter([c.x for c in Atom.atoms_list], [c.y for c in Atom.atoms_list], s=28**2, c='b',
                marker='o')
    plt.axis('off')
    plt.plot([0, 0, settings.width, settings.width, 0], [0, settings.height, settings.height, 0, 0], '-k')
    plt.draw()
    plt.pause(0.0000001)
    plt.clf()


print(matplotlib.rcParams['lines.markersize'])

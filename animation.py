import matplotlib.pyplot as plt
from atoms import AtomBlue as Atom
import settings


def draw():
    plt.axes(xlim=(0, settings.width), ylim=(0, settings.height))
    for a in Atom.atoms_list:
        plt.gcf().gca().add_artist(plt.Circle((a.x, a.y), settings.radius, color='b'))
    plt.axis('off')
    plt.plot([0, 0, settings.width, settings.width, 0], [0, settings.height, settings.height, 0, 0], '-k')
    plt.draw()
    plt.pause(settings.dt*00.1)
    plt.clf()

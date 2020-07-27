import matplotlib.pyplot as plt
from atoms import AtomBlue as Atom
import settings

def draw():
    plt.axes(xlim=(0, settings.width), ylim=(0, settings.height))
    plt.scatter([c.x for c in Atom.atoms_list], [c.y for c in Atom.atoms_list], s=100, c='b', marker='o')
    plt.axis('off')
    plt.plot([0,0,settings.width,settings.width,0],[0,settings.height,settings.height,0,0],'-k')
    plt.draw()
    plt.pause(0.01)
    plt.clf()


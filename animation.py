import matplotlib.pyplot as plt
import matplotlib as mpl
from atoms import AtomBlue as Atom
import settings


def draw():
    mpl.rcParams['toolbar'] = 'None'

    box = plt
    # box.style.use('dark_background')
    box.gcf().canvas.set_window_title("Symulator Zderzeń")
    box.axes(xlim=(0, settings.width), ylim=(0, settings.height))

    for a in Atom.atoms_list:
        if type(a) == Atom:
            box.gcf().gca().add_artist(plt.Circle((a.x, a.y), settings.radius, color='b'))
        else:
            box.gcf().gca().add_artist(plt.Circle((a.x, a.y), settings.radius, color='r'))

    box.plot([0, 0, settings.width, settings.width, 0], [0, settings.height, settings.height, 0, 0] , '-k')

    box.axis('scaled')
    box.axis(False)

    box.xticks([])
    box.yticks([])

    box.draw()
    box.pause(settings.dt*0.1)
    box.clf()

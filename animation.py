import matplotlib.pyplot as plt
import matplotlib as mpl
from atoms import AtomBlue as Atom
import settings
from matplotlib.widgets import TextBox, Button


def draw(x):

    if x == 1:
        mpl.rcParams['toolbar'] = 'None'
        plt.style.use('dark_background')
        plt.figure(figsize=(5, 4))
        def next(text):
            settings.atoms_number = int(text)

        def frames(text):
            settings.frames = int(text)

        def kappa(text):
            settings.k = int(text)

        def enter(event):
            plt.close('all')

        ax_atoms = plt.axes([0.4, 0.7, 0.2, 0.075])
        t_atoms = TextBox(ax_atoms, 'Atoms: ', color='r', hovercolor='firebrick')
        ax_frames = plt.axes([0.4, 0.6, 0.2, 0.075])
        t_frames = TextBox(ax_frames, 'Frames: ', color='r',hovercolor='firebrick')
        ax_kappa = plt.axes([0.4, 0.5, 0.2, 0.075])
        t_kappa = TextBox(ax_kappa, 'Kappa: ', color='r',hovercolor='firebrick')
        ax_button = plt.axes([0.7,0.3,0.2,0.075])
        bbutton = Button(ax_button,'Confirm',color='b',hovercolor='royalblue')
        bbutton.on_clicked(enter)
        t_atoms.on_submit(next)
        t_frames.on_submit(frames)
        t_kappa.on_submit(kappa)
        plt.text(-1.6,7.5,"Enter data",fontsize=18)
        plt.show()
    else:
        mpl.rcParams['toolbar'] = 'None'
        box = plt
        props = dict(boxstyle='round', facecolor='white', alpha=0.5)
        box.style.use('dark_background')
        box.gcf().canvas.set_window_title("Symulator Zderzeń")
        box.axes(xlim=(0, settings.width), ylim=(0, settings.height))
        for a in Atom.atoms_list:
            if type(a) == Atom:
                box.gcf().gca().add_artist(plt.Circle((a.x, a.y), settings.radius, color='b'))
            else:
                box.gcf().gca().add_artist(plt.Circle((a.x, a.y), settings.radius, color='r'))

        box.plot([0, 0, settings.width, settings.width, 0], [0, settings.height, settings.height, 0, 0], '-y')
        box.text(-6.5,15.5,"atoms: {}\n\nframes: {}\n\nKappa: {}".format(settings.atoms_number,settings.frames,settings.k),bbox=props)
        box.axis('scaled')
        box.axis(False)

        box.xticks([])
        box.yticks([])

        box.draw()
        box.pause(settings.dt)
        box.clf()


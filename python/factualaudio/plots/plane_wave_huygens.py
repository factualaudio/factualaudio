from matplotlib.patches import Circle
import numpy as np

def populate_figure(figure):
    figure.set_figheight(4)
    axes = figure.add_subplot(1, 1, 1)

    radius = 1
    axes.vlines(0, -1, 1, colors=['green'])
    axes.vlines(radius, -1, 1, colors=['red'])

    sources = np.linspace(-1 - radius, 1 + radius, 16);
    axes.plot(np.zeros(sources.size), sources, linestyle='None', marker='o', markerfacecolor='blue', markeredgecolor='blue')

    for pos in sources:
        axes.add_patch(Circle((0, pos), radius, facecolor='none', edgecolor='blue', linestyle=':'))
        axes.add_patch(Circle((0, pos), 0.05, facecolor='none', edgecolor='blue'))

    axes.set_aspect('equal')
    axes.set_xlim(-1.1, 2)
    axes.set_ylim(-1, 1)
    axes.set_axis_off()
    axes.annotate(xy=(radius * 1.5, 0), xytext=(radius, 0), s='', arrowprops={'shrink': 0.1, 'facecolor': 'black', 'edgecolor': 'none'})
    axes.annotate(xy=(0, -1), xytext=(0, -10), textcoords='offset points', s='Source', horizontalalignment='center', verticalalignment='top')
    axes.annotate(xy=(radius, -1), xytext=(0, -10), textcoords='offset points', s='Wavefront', horizontalalignment='center', verticalalignment='top')


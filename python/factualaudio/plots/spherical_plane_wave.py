from matplotlib.patches import Circle
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

def populate_figure(figure):
    figure.set_figheight(3)
    overview_axes = figure.add_subplot(1, 2, 1)
    zoom_axes = figure.add_subplot(1, 2, 2)

    for axes in [overview_axes, zoom_axes]:
        axes.set_aspect('equal')
        axes.set_xlim(-2, 2)
        axes.set_ylim(-2, 2)
        axes.plot(0, 0, linestyle='None', marker='o', markerfacecolor='green')
        axes.add_patch(Circle((0, 0), 0.15, facecolor='none', edgecolor='green'))
        axes.add_patch(Circle((0, 0), 1, facecolor='none', edgecolor='red'))

    overview_axes.set_axis_off()

    zoom_width = 0.1
    zoom_axes.set_xlim(1-zoom_width, 1+zoom_width)
    zoom_axes.set_ylim(-zoom_width, zoom_width)
    zoom_axes.set_xticks([])
    zoom_axes.set_yticks([])
    mark_inset(overview_axes, zoom_axes, loc1=2, loc2=3, linestyle='--')

    zoom_axes.vlines(1, -1, 1, linestyle=':', color='blue')
    zoom_axes.annotate(xy=(1 + zoom_width*0.75, 0), xytext=(1, 0), s='', arrowprops={'shrink': 0.1, 'facecolor': 'black', 'edgecolor': 'none'})


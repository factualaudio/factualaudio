import factualaudio.sound_field as sound_field
import factualaudio.sound_field_plot as sound_field_plot
import numpy as np
from matplotlib.gridspec import GridSpec
import matplotlib.cm as cm

def populate_snapshot(axes, cycle_count, show_labels=True):
    axes.set_title('t = ' + str(cycle_count) + ' periods')

    width_cycles = 3
    sound_field_plot.format_plot(axes, width_cycles)
    center = width_cycles / 2

    sound_field_plot.populate_source_markers(axes, [[center, center]])
    axes.annotate(s='', xy=[center, center], xytext=[center+1, center], arrowprops=dict(arrowstyle='|-|', shrinkA=0, shrinkB=0))
    if show_labels: axes.annotate(s='1 wavelength', xy=[center+0.5, center], xytext=[0, -15], horizontalalignment='center', verticalalignment='top', textcoords='offset pixels')

    return sound_field_plot.populate_heatmap(
            axes, np.real(sound_field.source_waveform_plane(
                sound_field.complex_plane()*width_cycles, sound_field.xy_to_complex([center, center]),
                cycle_count=cycle_count, spreading=False)),
            vmin=-1, vmax=1, cmap=cm.bwr)

def populate_figure(figure):
    figure.set_figheight(3)
    gs = GridSpec(2, 3, height_ratios=[16, 1])
    for i in [0, 1, 2]:
        image = populate_snapshot(figure.add_subplot(gs[0, i]), (i+1)/2, show_labels=i==0)
    figure.colorbar(image, orientation='horizontal', cax=figure.add_subplot(gs[1, :]), label='Relative instantaneous sound pressure')

from matplotlib.patches import Circle
from math import inf, sqrt
import numpy as np
from factualaudio.decibel import to_decibels
import factualaudio.geometry as geometry
import factualaudio.sound_field as sound_field
import factualaudio.sound_field_plot as sound_field_plot

speed_of_sound = 343
sound_field_size = 10
source_a = [3, 7]
source_b = [7, 7]
central_listener = [5, 2]
lateral_listener = [6, 2]

def populate_schematic(axes, use_lateral_listener=False):
    sound_field_plot.format_plot(axes, sound_field_size)
    listener = lateral_listener if use_lateral_listener else central_listener
    sound_field_plot.populate_source_markers(axes, [source_a, source_b])
    sound_field_plot.populate_listener_markers(axes, [central_listener] + ([lateral_listener] if use_lateral_listener else []))

    def add_source(xy, label):
        for radius in [1, 1.5]:
            axes.add_patch(Circle(xy, radius=radius, fill=False, linestyle=':'))
        axes.annotate(s=label, xy=xy, horizontalalignment='center', verticalalignment='bottom', textcoords='offset pixels', xytext=[0, 5])

    add_source(source_a, 'Source A')
    add_source(source_b, 'Source B')

    axes.annotate(s='Listener', xy=listener, horizontalalignment='center', verticalalignment='top', textcoords='offset pixels', xytext=[0, -5])
    axes.annotate(s='', xy=listener, xytext=source_a, arrowprops=dict(arrowstyle='->'))
    axes.annotate(s='', xy=listener, xytext=source_b, arrowprops=dict(arrowstyle='->'))
    
    axes.annotate(s='{:.1f} m'.format(geometry.distance(source_a, listener)), xy=geometry.midpoint(source_a, listener), horizontalalignment='right', verticalalignment='top', textcoords='offset pixels', xytext=[-5, -5])
    axes.annotate(s='{:.1f} m'.format(geometry.distance(source_b, listener)), xy=geometry.midpoint(source_b, listener), horizontalalignment='left', verticalalignment='top', textcoords='offset pixels', xytext=[5, -5])

def combined_waveform_plane(sources, frequency=250, *kargs, **kwargs):
    complex_plane = sound_field.complex_plane() * sound_field_size
    waveform_plane = complex_plane * 0
    for source in sources:
        waveform_plane += sound_field.source_waveform_plane(complex_plane, sound_field.xy_to_complex(source), wavelength=speed_of_sound / frequency, *kargs, **kwargs)
    return waveform_plane

def populate_amplitude(axes, sources=[source_a, source_b], listeners=[central_listener, lateral_listener], vmin=-20, vmax=6, title=None, *kargs, **kwargs):
    sound_field_plot.format_plot(axes, sound_field_size=sound_field_size)
    if title: axes.set_title(title)
    sound_field_plot.populate_source_markers(axes, sources)
    sound_field_plot.populate_listener_markers(axes, listeners)
    amplitude_decibels = to_decibels(np.fmax(np.abs(combined_waveform_plane(sources=sources, *kargs, **kwargs)), 1e-14))
    return sound_field_plot.populate_heatmap(axes, amplitude_decibels, vmin=vmin, vmax=vmax)

def populate_figure(figure):
    axes = figure.add_subplot(1, 1, 1)
    populate_schematic(axes)

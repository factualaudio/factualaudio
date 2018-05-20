import factualaudio.sound_field as sound_field
import factualaudio.sound_field_plot as sound_field_plot
from matplotlib.patches import Rectangle
from matplotlib.ticker import FuncFormatter
import numpy as np
import matplotlib.cm as cm

air_width = 21  # number of pockets
source_offset = 1
height = 5
total_width = source_offset + air_width
frequency = 1000
speed_of_sound = 343
wavelength = speed_of_sound / frequency
air_pocket_size = wavelength / (air_width-1)  # room for one cycle
displacement_factor = 0.9  # relative to air_pocket_size
displacement_amplitude = air_pocket_size * displacement_factor
acoustic_impedance = 413
pressure_amplitude = displacement_amplitude * frequency * np.pi * 2 * acoustic_impedance
scale_factor = 1000
initial_line_limit = 0.1

def populate_plane_wave_figure(figure, cycle_count, show_colorbar=False):
    figure.set_figheight(3.5)
    axes = figure.add_subplot(1, 1, 1)

    axes.set_xlim(0, total_width)
    axes.set_ylim(-0.5, height+0.5)
    axes.set_aspect('equal')
    axes.set_yticks([])
    axes.set_frame_on(False)

    # Displacement
    grid_distance_plane = sound_field.distance_plane(sound_field.complex_plane(total_width, 1, centered=False), source_offset/total_width)
    grid_displacement_plane = sound_field.waveform_plane(grid_distance_plane, cycle_count=cycle_count) * displacement_factor
    offsets = np.arange(source_offset, total_width)
    air_offsets = offsets[1:]
    displaced_offsets = offsets + np.real(grid_displacement_plane[0,source_offset:])
    displaced_source = displaced_offsets[0]
    displaced_air = displaced_offsets[1:]

    # Column labels
    axes.set_xticks(displaced_air - 0.5)
    axes.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: chr(ord('A') + pos)))
    axes.tick_params(bottom=False)

    # Source
    axes.vlines(source_offset, -1, height+1, linestyle=':', color='green')
    if (np.abs(displaced_source - source_offset) > initial_line_limit):
        axes.vlines(displaced_source, -1, 0, color='green', linestyle=':')
        axes.vlines(displaced_source, height, height+1, color='green', linestyle=':')
    axes.vlines(displaced_source, 0, height, color='green')

    # Vertical lines for grid
    axes.vlines(displaced_air, 0, height, color='grey')
    axes.vlines(displaced_air, -1, 0, color='grey', linestyle=':')
    axes.vlines(displaced_air, height, height+1, color='grey', linestyle=':')

    # Horizontal lines for grid
    axes.hlines(np.arange(height+1), displaced_source, displaced_air[-1], color='grey')
    axes.hlines(np.arange(height+1), displaced_air[-1], total_width, color='grey', linestyle=':')

    # Pressure heat map
    pixel_plane = sound_field.complex_plane(total_width*2, 1)
    pixel_distance_plane = sound_field.distance_plane(pixel_plane, source_offset/total_width) * (air_width/(air_width-1))
    scaled_pressure_amplitude = pressure_amplitude / scale_factor
    pixel_pressure_plane = sound_field.waveform_plane(pixel_distance_plane, cycle_count=cycle_count) * np.exp(-1j*np.pi/2) * scaled_pressure_amplitude
    heatmap = sound_field_plot.populate_heatmap(axes, np.real(pixel_pressure_plane), vmin=-scaled_pressure_amplitude, vmax=scaled_pressure_amplitude, cmap=cm.bwr)
    heatmap.set_clip_path(Rectangle((displaced_source, 0), displaced_air[-1]-displaced_source, height, transform=axes.transData))
    if show_colorbar:
        figure.colorbar(heatmap, label='Sound pressure (Pa)', orientation='horizontal')

    return (axes, displaced_source, displaced_air)

def populate_force(axes, fro, to, large=False, **kwargs):
    shrink = 5 if large else 7
    axes.annotate(s='', xy=to, xytext=fro, arrowprops=dict(facecolor='black', arrowstyle='wedge,tail_width=' + str(1 if large else 0.6), shrinkA=shrink, shrinkB=shrink, **kwargs), annotation_clip=False)

def populate_force_horizontal(axes, fro, length, **kwargs):
    populate_force(axes, fro, (fro[0]+length, fro[1]), **kwargs)

def populate_force_vertical(axes, fro, length, **kwargs):
    populate_force(axes, fro, (fro[0], fro[1]+length), **kwargs)

dual_offset=0.15

def populate_force_horizontal_dual(axes, xy, length=1, **kwargs):
    populate_force_horizontal(axes, (xy[0], xy[1]+dual_offset), length, **kwargs)
    populate_force_horizontal(axes, (xy[0]+length, xy[1]-dual_offset), -length, **kwargs)

def populate_force_vertical_dual(axes, xy, length=1, **kwargs):
    populate_force_vertical(axes, (xy[0]+dual_offset, xy[1]), length, **kwargs)
    populate_force_vertical(axes, (xy[0]-dual_offset, xy[1]+length), -length, **kwargs)

annotation_height = height + 1

def populate_ruler(axes, x1, x2, label=None):
    axes.annotate(s='', xy=(x1, height+1), xytext=(x2, annotation_height), arrowprops=dict(arrowstyle='|-|', shrinkA=0, shrinkB=0,mutation_scale=3), annotation_clip=False)
    if label is not None:
        axes.annotate(label, xy=(x2, annotation_height), annotation_clip=False, horizontalalignment='left', verticalalignment='center', textcoords='offset points', xytext=(5, 0))

def populate_figure(figure):
    (axes, displaced_source, displaced_air) = populate_plane_wave_figure(figure, cycle_count=0, show_colorbar=True)

    axes.annotate(s='Source', xy=(displaced_source, annotation_height), horizontalalignment='center', verticalalignment='center', annotation_clip=False)
    axes.annotate(s='Air', xy=(displaced_source + (total_width-displaced_source)/3, annotation_height), horizontalalignment='center', verticalalignment='center', annotation_clip=False)
    populate_ruler(axes, total_width-4, total_width-3, label='{:.0f} mm'.format(air_pocket_size * 1000))

    populate_force_horizontal_dual(axes, (displaced_source-0.5, height/2))
    populate_force_horizontal_dual(axes, (displaced_source+0.5, height/2))
    populate_force_vertical_dual(axes, (displaced_source+0.5, height/2))
    populate_force_vertical_dual(axes, (displaced_source+0.5, height/2-1))

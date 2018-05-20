from factualaudio.plots.plane_wave_initial import *

def populate_figure(figure):
    (axes, displaced_source, displaced_air) = populate_plane_wave_figure(figure, cycle_count=0.25)

    populate_ruler(axes, 1, displaced_source, '{:.0f} µm'.format((displaced_source - 1) * air_pocket_size * 1000000 / scale_factor))

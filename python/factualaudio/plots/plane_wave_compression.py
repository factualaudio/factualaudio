from factualaudio.plots.plane_wave_initial import *

def populate_figure(figure):
    (axes, displaced_source, displaced_air) = populate_plane_wave_figure(figure, cycle_count=0.05)

    populate_ruler(axes, source_offset, displaced_source, '{:.0f} µm'.format((displaced_source - source_offset) * air_pocket_size * 1000000 / scale_factor))

    for line in range(0, 5):
        populate_force_horizontal(axes, (displaced_source-0.5, line+0.5), 1, large=True)

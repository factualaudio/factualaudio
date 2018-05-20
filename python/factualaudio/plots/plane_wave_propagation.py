from factualaudio.plots.plane_wave_initial import *

def populate_figure(figure):
    (axes, displaced_source, displaced_air) = populate_plane_wave_figure(figure, cycle_count=0.1)

    axes.vlines(2, -1, height+1, color='grey', linestyle=':')
    populate_ruler(axes, 2, displaced_air[0], '{:.0f} µm'.format((displaced_air[0] - 2) * air_pocket_size * 1000000 / scale_factor))

    for line in range(0, 5):
        populate_force_horizontal(axes, (displaced_source-0.5, line+0.5), 1, large=True)
        populate_force_horizontal(axes, (displaced_air[0]-0.5, line+0.5), 1, large=True)

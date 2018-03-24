from factualaudio.plots.point_sources import populate_schematic

def populate_figure(figure):
    axes = figure.add_subplot(1, 1, 1)
    populate_schematic(axes, use_lateral_listener=True)

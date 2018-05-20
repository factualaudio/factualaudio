def format_plot(axes, sound_field_size=1):
    axes.set_xlim(0, sound_field_size)
    axes.set_ylim(0, sound_field_size)
    axes.set_aspect('equal')
    axes.set_xticks([])
    axes.set_yticks([])

def populate_source_markers(axes, sources):
    for source in sources:
        axes.plot(source[0], source[1], marker='o', markerfacecolor='C3', markeredgewidth=1, markeredgecolor='black')

def populate_listener_markers(axes, listeners):
    for listener in listeners:
        axes.plot(listener[0], listener[1], marker='s', markerfacecolor='C4', markeredgewidth=1, markeredgecolor='black')

def populate_heatmap(axes, amplitude_plane, xmin=None, xmax=None, ymin=None, ymax=None, *kargs, **kwargs):
    xmin = axes.get_xlim()[0] if xmin is None else xmin
    xmax = axes.get_xlim()[1] if xmax is None else xmax
    ymin = axes.get_ylim()[0] if ymin is None else ymin
    ymax = axes.get_ylim()[1] if ymax is None else ymax

    return axes.imshow(amplitude_plane, extent=[xmin, xmax, ymin, ymax], origin='lower', interpolation='bicubic', *kargs, **kwargs)


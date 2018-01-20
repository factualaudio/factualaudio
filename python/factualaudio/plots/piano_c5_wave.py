from factualaudio.data import piano_c5
from factualaudio.plots.sine_wave_1khz import populate_figure_wave

def populate_figure(figure):
    return populate_figure_wave(figure, *piano_c5())

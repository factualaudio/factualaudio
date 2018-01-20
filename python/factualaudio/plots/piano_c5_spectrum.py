from factualaudio.data import piano_c5
from factualaudio.plots.sine_spectrum_1khz import populate_figure_wave

def populate_figure(figure):
    return populate_figure_wave(figure, *piano_c5(), ymin=-25, ymax=-10)

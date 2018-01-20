import factualaudio.plots.sine_wave_amplitude_detail
import numpy as np

def populate_figure(figure):
    return factualaudio.plots.sine_wave_amplitude_detail.populate_figure(figure, lambda x: np.sinh(x*10) / np.sinh(10))

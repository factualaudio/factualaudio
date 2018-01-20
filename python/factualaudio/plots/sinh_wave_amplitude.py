import factualaudio.plots.sine_wave_amplitude
import numpy as np

def populate_figure(figure, *args, **kwargs):
    return factualaudio.plots.sine_wave_amplitude.populate_figure(figure, wavefilter=lambda x: np.sinh(x*10) / np.sinh(10), *args, **kwargs)

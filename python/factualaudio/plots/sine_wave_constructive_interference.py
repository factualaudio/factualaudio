from factualaudio.data import sine_wave
from factualaudio.plot_format import format_waveform_plot
from factualaudio.plot import waveform
from factualaudio.plots.sine_wave_sum import populate_figure_wavesum
import numpy as np

def populate_figure(figure):
    wave, sample_rate = sine_wave()
    return populate_figure_wavesum(figure, wave * (2 * np.sqrt(2)), wave * (5 * np.sqrt(2)), sample_rate)

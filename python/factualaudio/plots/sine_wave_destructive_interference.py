from factualaudio.data import sine_wave
from factualaudio.plot_format import format_waveform_plot
from factualaudio.plot import waveform
from factualaudio.plots.sine_wave_sum import populate_figure_wavesum
import numpy as np

def populate_figure(figure):
    wave1, sample_rate = sine_wave(phase_radians=np.pi)
    wave2, sample_rate = sine_wave(phase_radians=0)
    return populate_figure_wavesum(figure, wave1 * (2 * np.sqrt(2)), wave2 * (5 * np.sqrt(2)), sample_rate)
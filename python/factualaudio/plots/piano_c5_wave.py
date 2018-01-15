from factualaudio.plot_format import format_waveform_plot
from factualaudio.data import piano_c5
import numpy as np

def populate_figure(figure):
    wave, sample_rate = piano_c5()
    axes = figure.add_subplot(1, 1, 1)
    axes.plot(np.arange(0, wave.size) / sample_rate * 1000, wave)
    format_waveform_plot(figure)

from factualaudio.plot_format import format_waveform_plot
from factualaudio.data import piano_c5
import numpy as np

def populate_figure(figure):
    y, sample_rate = piano_c5()
    x = np.arange(0, y.size) / sample_rate * 1000
    axes = figure.add_subplot(1, 1, 1)
    axes.plot(x, y)
    format_waveform_plot(figure)

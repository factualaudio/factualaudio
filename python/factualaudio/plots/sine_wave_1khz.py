from factualaudio.plot_format import format_waveform_plot
import numpy as np

def populate_figure(figure):
    x = np.linspace(0, 3, num=100)
    y = np.sin(x * np.pi * 2)
    axes = figure.add_subplot(1, 1, 1)
    axes.plot(x, y)
    format_waveform_plot(figure)

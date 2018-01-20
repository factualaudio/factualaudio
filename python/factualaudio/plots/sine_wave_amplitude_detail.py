from factualaudio.data import sine_wave
from factualaudio.plot_format import format_waveform_plot, annotate_amplitude
import numpy as np

def populate_figure(figure, wavefilter=lambda x: x):
    num_periods = 3
    wave = wavefilter(sine_wave(num_periods=num_periods))
    axes = figure.add_subplot(1, 1, 1)
    axes.plot(np.linspace(0, num_periods, endpoint=False, num=wave.size), wave)
    format_waveform_plot(figure)
    annotate_amplitude(axes, wave)

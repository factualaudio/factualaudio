from factualaudio.data import sine_wave
from factualaudio.plot_format import format_waveform_plot
import numpy as np

def populate_figure(figure):
    num_periods = 3
    wave = sine_wave(num_periods=num_periods)
    axes = figure.add_subplot(1, 1, 1)
    axes.plot(np.linspace(0, num_periods, endpoint=False, num=wave.size), wave)
    format_waveform_plot(figure)

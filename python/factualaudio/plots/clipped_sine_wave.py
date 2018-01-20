from factualaudio.data import sine_wave
from factualaudio.plot_format import format_waveform_plot
from factualaudio.plot import waveform
import numpy as np

def clipped_sine_wave(num_periods):
    samples_per_period = 100
    wave, sample_rate = sine_wave(frequency=1000, num_periods=num_periods)
    return np.fmin(np.fmax(wave * 1.2, -1), 1), sample_rate

def populate_figure(figure):
    waveform(figure.add_subplot(1, 1, 1), *clipped_sine_wave(num_periods=3))
    format_waveform_plot(figure)

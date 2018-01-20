from factualaudio.data import sine_wave, noise
from factualaudio.plot_format import format_waveform_plot
import numpy as np

def noisy_sine_wave(num_periods):
    samples_per_period = 100
    wave = sine_wave(num_periods=num_periods, samples_per_period=100)
    return wave + noise(wave.size) * 0.5, samples_per_period*1000

def populate_figure(figure):
    wave, sample_rate = noisy_sine_wave(num_periods=3)
    axes = figure.add_subplot(1, 1, 1)
    axes.plot(np.arange(0, wave.size) * (1000 / sample_rate), wave)
    format_waveform_plot(figure)

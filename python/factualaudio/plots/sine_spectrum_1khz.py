from factualaudio.data import sine_wave
from factualaudio.plot_format import format_spectrum
from factualaudio.plot import rms_amplitude_spectrum
import numpy as np

def populate_figure_wave(figure, wave, sample_rate, ymin, ymax):
    axes = figure.add_subplot(1, 1, 1)
    rms_amplitude_spectrum(axes, wave, Fs=sample_rate)
    format_spectrum(figure)
    axes.set_ylim(ymin, ymax)
    axes.set_yticks([])
    axes.set_ylabel("Amplitude")

def populate_figure(figure):
    return populate_figure_wave(figure, *sine_wave(frequency=1000), ymin=-20, ymax=0)


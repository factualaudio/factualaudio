from factualaudio.data import sine_wave
from factualaudio.plot_format import format_spectrum
from factualaudio.plot import rms_amplitude_spectrum
import numpy as np

def populate_figure(figure):
    wave, sample_rate = sine_wave(frequency=1000)

    axes = figure.add_subplot(1, 1, 1)
    rms_amplitude_spectrum(axes, wave, Fs=sample_rate)
    format_spectrum(figure)
    axes.set_ylim(-20, 0)


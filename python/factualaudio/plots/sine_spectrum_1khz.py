from factualaudio.data import sine_wave, noise
from factualaudio.decibel import to_decibels
from factualaudio.plot_format import format_spectrum
from factualaudio.plot import rms_amplitude_spectrum
import numpy as np

def populate_figure(figure):
    samples_per_period = 100

    wave = sine_wave(num_periods=3, samples_per_period=samples_per_period)

    axes = figure.add_subplot(1, 1, 1)
    rms_amplitude_spectrum(axes, wave, Fs=samples_per_period * 1000, window=np.ones(wave.size), scale='dB')
    format_spectrum(figure)
    axes.set_ylim(-20, 0)


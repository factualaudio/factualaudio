from factualaudio.plots.noisy_sine_wave import noisy_sine_wave
from factualaudio.plot_format import format_spectrum, add_ellipse_annotation
from factualaudio.plot import rms_amplitude_spectrum
import numpy as np

def populate_figure(figure):
    wave, sample_rate = noisy_sine_wave(num_periods=100)

    axes = figure.add_subplot(1, 1, 1)
    rms_amplitude_spectrum(axes, wave, Fs=sample_rate)
    format_spectrum(figure)
    axes.set_ylim(-80, 10)
    add_ellipse_annotation(figure, xy=(0.5, 0.35), width=1.1, height=0.3, transform=axes.transAxes)

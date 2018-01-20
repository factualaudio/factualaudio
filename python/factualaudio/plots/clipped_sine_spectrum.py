from factualaudio.plots.clipped_sine_wave import clipped_sine_wave
from factualaudio.plot_format import format_spectrum, add_ellipse_annotation
from factualaudio.plot import rms_amplitude_spectrum
import numpy as np

def populate_figure(figure):
    wave, sample_rate = clipped_sine_wave(num_periods=3)

    axes = figure.add_subplot(1, 1, 1)
    rms_amplitude_spectrum(axes, wave, Fs=sample_rate)
    format_spectrum(figure)
    axes.set_ylim(-60, 0)
    axes.set_xticks(np.array([1, 3, 5, 7, 9])*1000)
    axes.set_xticklabels(['1k', '3k', '5k', '7k', '9k'])
    axes.set_xticks([], minor=True)
    add_ellipse_annotation(figure, xy=(0.8, 0.3), width=0.4, height=0.8, transform=axes.transAxes)

from factualaudio.data import sine_wave
from factualaudio.plot_format import format_waveform_plot, annotate_amplitude
from factualaudio.plot import waveform
import numpy as np

def populate_figure(figure, wavefilter=lambda x: x):
    wave, sample_rate = sine_wave(frequency=1000, num_periods=3)
    wave = wavefilter(wave)
    axes = figure.add_subplot(1, 1, 1)
    waveform(axes, wave, sample_rate)
    format_waveform_plot(figure)
    annotate_amplitude(axes, wave)
    axes.set_xticks([])
    axes.set_xlabel('')
    axes.set_ylabel('')

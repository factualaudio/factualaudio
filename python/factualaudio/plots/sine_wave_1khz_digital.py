from factualaudio.data import sine_wave
from factualaudio.plot_format import format_waveform_plot
from factualaudio.plot import waveform
import numpy as np

def populate_figure(figure):
    axes = figure.add_subplot(1, 1, 1)
    wave, sample_rate = sine_wave(num_periods=2, samples_per_period=44.1)
    axes.stem(wave * 32767, markerfmt='.', basefmt=' ')
    format_waveform_plot(figure)
    axes.set_xlabel('Time (samples)')
    axes.set_ylabel('Sample value')
    axes.set_yticks([-32767, -16384, 0, 16384, 32767])

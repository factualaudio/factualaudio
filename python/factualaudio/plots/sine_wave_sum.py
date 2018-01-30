from factualaudio.data import sine_wave
from factualaudio.plot_format import format_waveform_plot
from factualaudio.plot import waveform
import numpy as np

from factualaudio.plot_format import annotate_amplitude

def populate_figure_wavesum(figure, wave1, wave2, sample_rate):
    axes = figure.add_subplot(1, 1, 1)
    wavesum = wave1 + wave2

    waveform(axes, wave1, sample_rate, label='Wave 1')
    waveform(axes, wave2, sample_rate, label='Wave 2')
    waveform(axes, wavesum, sample_rate, label='Sum')

    format_waveform_plot(figure)
    axes.legend(loc='upper right')
    axes.set_xticks([])
    axes.set_xlabel('Time')
    axes.set_ylim(-10, 10)

def populate_figure(figure):
    wave1, sample_rate = sine_wave(frequency=1000, phase_radians=0, num_periods=2, samples_per_period=250)
    wave2, sample_rate = sine_wave(frequency=2500, phase_radians=np.pi/3, num_periods=5, samples_per_period=100)
    return populate_figure_wavesum(figure, wave1 * 5, wave2 * 3, sample_rate)

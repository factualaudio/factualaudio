from factualaudio.plots.point_sources_amplitude_transient import populate_waveform
from factualaudio.data import sine_wave
from factualaudio.plot_format import format_waveform_plot
from factualaudio.plot import waveform
from factualaudio.decibel import from_decibels
import numpy as np

def populate_figure(figure):
    axes = figure.add_subplot(1, 1, 1)
    populate_waveform(axes)
    format_waveform_plot(figure)
    axes.set_ylabel('Relative sound pressure')



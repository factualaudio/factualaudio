from factualaudio.data import sine_wave
from factualaudio.plot_format import format_waveform_plot
from factualaudio.plot import waveform

def populate_figure_wave(figure, wave, sample_rate):
    axes = figure.add_subplot(1, 1, 1)
    waveform(axes, wave, sample_rate)
    format_waveform_plot(figure)
    axes.set_yticks([])

def populate_figure(figure):
    return populate_figure_wave(figure, *sine_wave(frequency=1000, num_periods=3))

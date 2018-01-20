from factualaudio.data import sine_wave
from factualaudio.plot_format import format_waveform_plot
from factualaudio.plot import waveform

def populate_figure(figure):
    waveform(figure.add_subplot(1, 1, 1), *sine_wave(frequency=1000, num_periods=3))
    format_waveform_plot(figure)

from factualaudio.plot_format import format_waveform_plot
from factualaudio.plot import waveform
from factualaudio.data import piano_c5

def populate_figure(figure):
    axes = figure.add_subplot(1, 1, 1)
    waveform(axes, *piano_c5())
    format_waveform_plot(figure)
    axes.set_yticks([])

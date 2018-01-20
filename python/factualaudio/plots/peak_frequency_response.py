from factualaudio.plot_format import format_spectrum
from factualaudio.plot import transfer_function_gain
from factualaudio.rbj import peak

def populate_figure(figure):
    axes = figure.add_subplot(1, 1, 1)
    transfer_function_gain(axes, peak(2, 2), corner_frequency=1000)
    format_spectrum(figure)
    axes.set_ylim(-10, 10)
    axes.set_ylabel('Gain (dB)')

from factualaudio.plot_format import format_spectrum
from factualaudio.plot import transfer_function_phase
from factualaudio.rbj import peak

def populate_figure(figure):
    axes = figure.add_subplot(1, 1, 1)
    transfer_function_phase(axes, peak(peak_gain=12, Q=1), corner_frequency=1000)
    format_spectrum(figure)
    axes.set_ylim(-180, 180)
    axes.set_ylabel('Phase shift (degrees)')

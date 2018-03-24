from factualaudio.plots.point_sources import populate_amplitude

def populate_figure(figure):
    figure.colorbar(populate_amplitude(figure.add_subplot(1, 1, 1)), label='Amplitude (dB)')

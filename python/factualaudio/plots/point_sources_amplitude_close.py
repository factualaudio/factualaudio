from factualaudio.plots.point_sources import populate_amplitude

def populate_figure(figure):
    figure.colorbar(populate_amplitude(figure.add_subplot(1, 1, 1), sources=[[4.85, 7], [5.15, 7]]), label='Amplitude (dB)')

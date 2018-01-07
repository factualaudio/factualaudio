from factualaudio.data import sine_wave
from factualaudio.plots.sine_wave_1khz_phase import plots
from factualaudio.plot_format import format_spectrum
import numpy as np

def populate_figure(figure):
    axes = figure.add_subplot(1, 1, 1)
    for plot in plots:
        axes.plot([1000], [plot['phase_degrees']], marker=plot['marker'], linestyle=' ', color=plot['color'], label=str(plot['phase_degrees']) + '°')
    format_spectrum(figure)
    axes.legend(loc='upper right')
    axes.set_ylim(0, 360)
    axes.set_ylabel('Phase (degrees)')


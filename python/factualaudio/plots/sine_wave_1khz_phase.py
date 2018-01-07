from factualaudio.data import sine_wave
from factualaudio.plot_format import format_waveform_plot
from factualaudio.plot import waveform
import numpy as np

plots = [
        {'phase_degrees': 0, 'linestyle': '-', 'marker': 'o', 'color': '#1f77b4'},
        {'phase_degrees': 90, 'linestyle': '-.', 'marker': 's', 'color': '#ff7f0e'},
        {'phase_degrees': 180, 'linestyle': '--', 'marker': 'x', 'color': '#2ca02c'},
        {'phase_degrees': 270, 'linestyle': ':', 'marker': '+', 'color': '#d62728'},
]

def populate_figure(figure):
    axes = figure.add_subplot(1, 1, 1)
    # These are the default matplotlib colors, but we're hardcoding them
    # because they are mentioned explicitly in the accompanying text.
    for plot in plots:
        wave, sample_rate = sine_wave(frequency=1000, num_periods=2, phase_radians=np.radians(plot['phase_degrees']))
        waveform(axes, wave, sample_rate, linestyle=plot['linestyle'], color=plot['color'], label=str(plot['phase_degrees']) + '°')
    format_waveform_plot(figure)
    axes.legend(loc='upper right')
    axes.set_yticks([])

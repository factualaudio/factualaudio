from factualaudio.data import sine_wave
import factualaudio.geometry as geometry
from factualaudio.plots.point_sources import populate_amplitude
from factualaudio.plot import waveform
from factualaudio.plot_format import format_waveform_plot
from matplotlib.gridspec import GridSpec
from math import inf
import numpy as np

frequency = 250
sources = [[3, 4], [7, 8]]
listener = [5, 2]

def populate_subplot(axes, cycle_count=inf, *kargs, **kwargs):
    return populate_amplitude(
            axes, sources=sources, listeners=[listener], vmin=-15, vmax=6, cycle_count=cycle_count, frequency=frequency,
            title=('t = ' + '{:.0f}'.format(cycle_count*1000/250) + ' ms') if cycle_count != inf else 'Steady state',
            *kargs, **kwargs)

def populate_figure(figure):
    gs = GridSpec(2, 3, width_ratios=[16, 16, 1])
    populate_subplot(figure.add_subplot(gs[0, 0]), cycle_count=2)
    populate_subplot(figure.add_subplot(gs[0, 1]), cycle_count=4)
    populate_subplot(figure.add_subplot(gs[1, 0]), cycle_count=5)
    image = populate_subplot(figure.add_subplot(gs[1, 1]))
    colorbar_axes = figure.add_subplot(gs[:, 2])
    figure.colorbar(image, cax=colorbar_axes, label='Amplitude (dB)')

def populate_waveform(axes):
    speed_of_sound = 343
    length = 0.03
    num_periods = int(length * frequency)
    base_wave, sample_rate = sine_wave(frequency=frequency, num_periods=num_periods)
    length_samples = int(length * sample_rate)

    wave = np.zeros(length_samples)
    for source in sources:
        distance = geometry.distance(source, listener)
        delay = distance / speed_of_sound
        wave += np.pad(base_wave / distance, int(sample_rate * delay), mode='constant')[:length_samples]
        axes.axvline(delay * 1000, linestyle='--', color='C1')

    waveform(axes, wave, sample_rate)

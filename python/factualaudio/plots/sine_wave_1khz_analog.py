from factualaudio.data import sine_wave
from factualaudio.plot_format import format_waveform_plot
from factualaudio.plot import waveform

def populate_figure(figure):
    axes = figure.add_subplot(1, 1, 1)
    wave, sample_rate = sine_wave(frequency=1000, num_periods=2)
    waveform(axes, wave*1.41, sample_rate)
    format_waveform_plot(figure)
    axes.set_ylabel('Voltage (volts)')

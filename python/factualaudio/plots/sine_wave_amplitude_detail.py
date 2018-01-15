from factualaudio.data import sine_wave
from factualaudio.plot_format import format_waveform_plot
import numpy as np

def populate_figure(figure):
    num_periods = 3
    wave = sine_wave(num_periods=num_periods)
    axes = figure.add_subplot(1, 1, 1)
    axes.plot(np.linspace(0, num_periods, endpoint=False, num=wave.size), wave)
    format_waveform_plot(figure)

    axes.axhline(-1, linestyle=':')
    axes.axhline(1/np.sqrt(2), linestyle=':')
    axes.axhline(1, linestyle=':')

    def arrow_with_text(x, y1, y2, text):
        axes.annotate(text, xy=(x, 0), textcoords=('offset points'), xytext=(-5, 5), horizontalalignment='right')
        axes.annotate("", xy=(x, y1), xytext=(x, y2), arrowprops=dict(arrowstyle="<->"))

    arrow_with_text(1.3, -1, 1, "Peak-to-peak")
    arrow_with_text(1.8, 0, 1, "Peak")
    arrow_with_text(2.3, 0, 1/np.sqrt(2), "RMS")

import numpy as np
from matplotlib.patches import Ellipse
from matplotlib.ticker import ScalarFormatter

def format_waveform_plot(figure):
    figure.set_figheight(2.5)
    axes = figure.axes[0]
    axes.autoscale(axis='x', tight=True)
    axes.axhline(color='gray', zorder=0)
    axes.set_xlabel('Time (milliseconds)')
    axes.set_ylabel('Amplitude')

def format_spectrum(figure):
    figure.set_figheight(4)
    axes = figure.axes[0]
    axes.set_xscale("log")
    axes.set_xlim(20, 20000)
    axes.set_xlabel('Frequency (Hz)')
    axes.set_ylabel('Amplitude (dB)')
    axes.set_xticks([20, 100, 1000, 10000, 20000])
    axes.get_xaxis().set_major_formatter(ScalarFormatter())

# Adds an annotation in the form of an ellipse.
# Note that you probably want to use either transform=axes.transData or
# transform=transAxes depending on your use case.
def add_ellipse_annotation(figure, *args, **kwargs):
    kwargs.setdefault("edgecolor", "red")
    kwargs.setdefault("fill", False)
    kwargs.setdefault("linewidth", 2)
    # We add to the figure, not the axes, so that the patch is draw on
    # top of everything else and is not constrained by the axes box.
    return figure.patches.append(Ellipse(*args, **kwargs))

def annotate_amplitude(axes, wave):
    wavemin = np.amin(wave)
    wavemax = np.amax(wave)
    waverms = np.sqrt(np.mean(np.square(wave)))

    for value in [wavemin, wavemax, waverms]:
        axes.axhline(value, linestyle=':')

    def arrow_with_text(x, y1, y2, text):
        axes.annotate(text, xy=(x, 0), textcoords=('offset points'), xytext=(-5, 5), horizontalalignment='right')
        axes.annotate("", xy=(x, y1), xytext=(x, y2), arrowprops=dict(arrowstyle="<->"))

    arrow_with_text(1.3, wavemin, wavemax, "Peak-to-peak")
    arrow_with_text(1.8, 0, wavemax, "Peak")
    arrow_with_text(2.3, 0, waverms, "RMS")

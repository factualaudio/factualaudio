def format_waveform_plot(figure):
    figure.set_figheight(2)
    axes = figure.axes[0]
    axes.autoscale(axis='x', tight=True)
    axes.axhline(color='gray', zorder=0)

def format_spectrum(figure):
    axes = figure.axes[0]
    axes.set_xscale("log")
    axes.set_xlim(20, 20000)

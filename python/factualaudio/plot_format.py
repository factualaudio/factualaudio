def format_waveform_plot(figure):
    figure.set_figheight(2)
    axes = figure.axes[0]
    axes.autoscale(axis='x', tight=True)
    axes.axhline(color='gray', zorder=0)

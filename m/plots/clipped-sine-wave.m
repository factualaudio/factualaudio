fplot(@(x) min(max(sin(x*pi*2) * 1.2, -1), 1), [0, 3]);
format_waveform_plot();
set(gca(), 'ylim', [-1.2 1.2]);
set(gca(), 'ytick', []);
set(gca(), 'ylabel', '');


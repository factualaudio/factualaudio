fplot(@(x) sin(x*pi*2), [0, 3]);
format_waveform_plot();
set(gca(), 'xlabel', '');
set(gca(), 'xtick', []);
set(gca(), 'ylim', [-1.5 1.5]);

fplot(@(x) sinh(sin(x*pi*2)*10)/sinh(10), [0, 3], 1000);
format_waveform_plot();
set(gca(), 'xlabel', '');
set(gca(), 'xtick', []);
set(gca(), 'ylim', [-1.5 1.5]);


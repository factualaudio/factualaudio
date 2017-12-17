fplot(@(x) sin(x*pi*2), [0, 3]);
line([0 3], [0 0]);
format_waveform_plot();
set(gca(), 'ytick', []);
set(gca(), 'ylabel', 'Amplitude');

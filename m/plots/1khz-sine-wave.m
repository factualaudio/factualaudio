fplot(@(x) sin(x*pi*2), [0, 3]);
format_waveform_plot();
set(gca(), 'ytick', []);
set(gca(), 'ylabel', 'Amplitude');

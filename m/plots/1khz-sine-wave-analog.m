% When the third parameter is omitted, the plot is not granular enough. Go figure.
fplot(@(x) sin(x*pi*2) * 1.41, [0, 2], 4);
format_waveform_plot();
set(gca(), 'ylabel', 'Voltage (volts)');

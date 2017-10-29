function plot_transfer_function_gain(transfer_function, corner_frequency)
	fplot(@(x) mag2db(abs(transfer_function(i .* x / corner_frequency))), [0 20000]);
	format_spectrum_plot();
	set(gca(), 'ylabel', 'Gain (dB)');
	set(gca(), 'ylim', [-10 10]);
endfunction

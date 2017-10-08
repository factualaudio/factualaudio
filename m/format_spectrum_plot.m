function format_spectrum_plot
	format_plot();
	set_plot_height(0.5);
	set(gca(), 'xlabel', 'Frequency (Hz)');
	set(gca(), 'xlim', [20 20000]);
	set(gca(), 'xscale', 'log');
	ticks = [20 100 1000 10000 20000];
	set(gca(), 'xtick', ticks);
	set(gca(), 'xticklabel', cellstr(num2str(ticks', '%.0f')));
endfunction


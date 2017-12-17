function format_waveform_plot
	format_plot();
	set_plot_height(0.3);
	set(gca(), 'xlabel', 'Time (milliseconds)');
	line(xlim(), [0 0]);
endfunction


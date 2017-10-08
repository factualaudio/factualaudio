% Sets the plot height to factor * width, keeping the width constant so that the
% font size is consistent between different plots.
function set_plot_height(factor)
	plot_width = 600;
	plot_height = plot_width * factor;

	set(gcf(), 'paperunits', 'points');
	set(gcf(), 'paperposition', [ 0 0 plot_width plot_height ]);
endfunction

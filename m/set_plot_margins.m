% Enforces consistent margins around the axes for all plots.
%
% This seems like something Octave should be able to take care of for us, but
% it doesn't. Well, actually, it kinda does if we use the gnuplot toolkit, but
% then that opens a whole other can of worms.
function set_plot_margins()
	% Avoid repeated calls, as this function is not idempotent
	% (see margin adjustement code, below).
	persistent already_called = false;
	if (already_called)
		return;
	endif
	already_called = true;

	paperposition = get(gcf(), 'paperposition');
	plot_width = paperposition(3);
	plot_height = paperposition(4);

	% Use absolute, not relative, margins for consistency.
	left_margin = 60;
	right_margin = 40;
	top_margin = 5;
	bottom_margin = 50;

	left_adjust = 0;
	right_adjust = 0;
	top_adjust = 0;
	bottom_adjust = 0;

	% Avoid leaving too much white space when the X axis is not annotated.
	if (length(get(gca(), 'xtick')) == 0)
		bottom_adjust -= 20;
	endif

	left_margin += left_adjust;
	right_margin += right_adjust;
	top_margin += top_adjust;
	bottom_margin += bottom_adjust;

	axes_position = [
		left_margin / plot_width ...
		bottom_margin / plot_height ...
		(plot_width - left_margin - right_margin) / plot_width ...
		(plot_height - bottom_margin - top_margin) / plot_height ...
	];
	set(gca(), 'position', axes_position);

	% If we've made special adjustments to the margins, change the figure size
	% so that the size of the axes stay consistent between plots.
	plot_width += left_adjust + right_adjust;
	plot_height += top_adjust + bottom_adjust;
	set(gcf(), 'paperposition', [ 0 0 plot_width plot_height ]);
endfunction

function generate_plot()
	% We don't care about "true" randomness. It's more desirable to
	% have deterministic output that doesn't change.
	rand('state', 0);

	graphics_toolkit('fltk');
	set(gcf(), 'visible', 'off');
	source([ 'plots/' getenv('PLOTNAME') '.m' ]);
	set_plot_margins();
	print([ getenv('PLOTBASENAME') '.svg' ], '-dsvg');
	print([ getenv('PLOTBASENAME') '.png' ], '-dpng');
endfunction

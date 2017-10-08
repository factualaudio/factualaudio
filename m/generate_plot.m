function generate_plot()
	graphics_toolkit('fltk');
	set(gcf(), 'visible', 'off');
	source([ 'plots/' getenv('PLOTNAME') '.m' ]);
	set_plot_margins();
	print(getenv('PLOTSVGPATH'), '-dsvg');
endfunction

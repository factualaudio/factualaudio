function h = horizontal_line(height)
	h = line([0 xlim()(2)], [height height]);
	set(h, 'linestyle', '--');
endfunction

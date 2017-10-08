function [arrow, label] = vertical_annotation(x, y, text_y, text)
	arrow = data_annotation('doublearrow', [ x x ], y);

	label = data_annotation('textbox', [ x text_y 0 0 ]);
	set(label, 'horizontalalignment', 'right');
	set(label, 'string', text);

	label_position = get(label, 'position');
	label_position(1) *= 0.975;
	set(label, 'position', label_position);
endfunction

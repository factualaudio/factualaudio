%
% Draws an annotation using coordinates referred to the data axes,
% as opposed to normalized figure coordinates.
%
% This is an attempt to fill the Octave feature gap described in:
%   https://savannah.gnu.org/bugs/index.php?52185
%
% Note that the size of the figure or axes can't be changed after this
% function is called. For this reason it is recommended to add annotations
% as the very last step.
%
% CAUTION: in order for this function to work with gnuplot, the axes
% 'position' property needs to be set explicitly - if you try to use
% it with default axes position (automatic positioning), the
% coordinates will be off. See:
%   https://savannah.gnu.org/bugs/index.php?52184
% (this is not a problem when using any other graphics toolkit)
%
function h = data_annotation(name, varargin)
	% Try to make sure size of the figure and axes are final.
	set_plot_margins();

	x_offset = xlim()(1);
	x_factor = diff(xlim());
	y_offset = ylim()(1);
	y_factor = diff(ylim());

	axes_position = get(gca(), 'position');
	axes_x = axes_position(1);
	axes_y = axes_position(2);
	axes_width = axes_position(3);
	axes_height = axes_position(4);

	switch (length(varargin))
		case 1
			pos = varargin{1};

			% Normalize coordinates relative to data limits
			pos = [ (pos(1) - x_offset) / x_factor (pos(2) - y_offset) / y_factor pos(3:end) ];

			% Translate normalized axis coordinates to figure coordinates
			pos = [ pos(1) * axes_width + axes_x pos(2) * axes_height + axes_y pos(3:end) ];

			h = annotation(name, pos);
		case 2
			% Normalize coordinates relative to data limits
			x = (varargin{1} - x_offset) / x_factor;
			y = (varargin{2} - y_offset) / y_factor;

			% Translate normalized axis coordinates to figure coordinates
			x = x * axes_width + axes_x;
			y = y * axes_height + axes_y;

			h = annotation(name, x, y);
	endswitch
endfunction

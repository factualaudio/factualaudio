import argparse
import importlib
import io
import os
from matplotlib.figure import Figure
from matplotlib import rcParams

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('plot_module', help='qualified plot module name')
argument_parser.add_argument('--png-output', help='path to output PNG file')
argument_parser.add_argument('--svg-output', help='path to output SVG file')
argument_parser.add_argument('--svg-preamble', help='insert text right after XML declaration', action='append')
args = argument_parser.parse_args()

# Ensure the SVG output is deterministic. We use the module name as part
# of the salt so that multiple SVG plots can be combined without ID
# conflicts, in case anyone ever feels like doing that.
rcParams['svg.hashsalt'] = 'factualaudio.com/' + args.plot_module

figure = Figure(tight_layout=True)

plot_module = importlib.import_module(args.plot_module)
plot_module.populate_figure(figure)

if args.png_output is not None:
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    FigureCanvasAgg(figure).print_png(args.png_output)

if args.svg_output is not None:
    from matplotlib.backends.backend_svg import FigureCanvasSVG
    if args.svg_preamble is None:
        FigureCanvasSVG(figure).print_svg(args.svg_output)
    else:
        svg = io.BytesIO()
        FigureCanvasSVG(figure).print_svg(svg)
        svg.seek(0)

        svg_file = open(args.svg_output, 'wb')
        first_line = True
        for svg_line in svg:
            svg_file.write(svg_line)
            if first_line:
                for svg_preamble in args.svg_preamble:
                    svg_file.write((svg_preamble + os.linesep).encode())
                first_line = False


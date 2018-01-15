import argparse
import importlib
from matplotlib.figure import Figure
from matplotlib import rcParams

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('plot_module', help='qualified plot module name')
argument_parser.add_argument('--png-output', help='path to output PNG file')
argument_parser.add_argument('--svg-output', help='path to output SVG file')
args = argument_parser.parse_args()

# Ensure the SVG output is deterministic. We use the module name as part
# of the salt so that multiple SVG plots can be combined without ID
# conflicts, in case anyone ever feels like doing that.
rcParams['svg.hashsalt'] = 'factualaudio.com/' + args.plot_module

figure = Figure()

plot_module = importlib.import_module(args.plot_module)
plot_module.populate_figure(figure)

if args.png_output is not None:
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    FigureCanvasAgg(figure).print_png(args.png_output)

if args.svg_output is not None:
    from matplotlib.backends.backend_svg import FigureCanvasSVG
    FigureCanvasSVG(figure).print_svg(args.svg_output)


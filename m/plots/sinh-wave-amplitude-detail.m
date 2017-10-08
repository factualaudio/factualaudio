indices = [0:0.001:3];
samples = sinh(sin(indices*pi*2)*10)/sinh(10);

plot(indices, samples);
format_waveform_plot();
set(gca(), 'xlabel', '');
set(gca(), 'xtick', []);
set(gca(), 'ylim', [-1.5 1.5]);

annotate_amplitude(samples);

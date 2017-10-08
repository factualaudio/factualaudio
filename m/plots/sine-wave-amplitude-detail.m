indices = [0:0.01:3];
samples = sin(indices*pi*2);

plot(indices, samples);
format_waveform_plot();
set(gca(), 'xlabel', '');
set(gca(), 'xtick', []);
set(gca(), 'ylim', [-1.5 1.5]);

annotate_amplitude(samples);

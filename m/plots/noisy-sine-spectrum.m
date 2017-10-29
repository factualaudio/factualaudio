sample_rate = 48000;
samples = repmat(sine_wave_cycle(1000, sample_rate), 1, 100);
samples += (rand(1, length(samples)) - 0.5) * 0.5;
plot_fft(samples, sample_rate, 1);
format_spectrum_plot();
set(gca(), 'ylabel', 'Amplitude (dB)');
set(gca(), 'ylim', [-80 10]);
set(gca(), 'xlabel', '');
set(gca(), 'xtick', []);

a = annotation('ellipse', [ 0.05 0.2 0.925 0.3 ]);
set(a, 'linewidth', 2);
set(a, 'edgecolor', 'red');

